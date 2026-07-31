<#
.SYNOPSIS
    Startet die Supervisor-Anwendung und gleicht vorher das Programmverzeichnis
    aus der Ablage "ProgrammAA" mit dem lokalen Arbeitsverzeichnis ab.

.DESCRIPTION
    Ersatz fuer StartSupervisor.exe.

    Wichtigste Aenderung gegenueber der bisherigen Version:
    Die Datenbanken einsatz.mdb und faktbasis.mdb werden beim Abgleich
    NIE ueberschrieben. Sie werden ausschliesslich dann aus der Quelle
    kopiert, wenn sie lokal noch gar nicht vorhanden sind (Erstinstallation).
    Damit gehen lokale Daten bei einem Programm-Update nicht mehr verloren.

    Ablauf:
      1. Quelle und Ziel bestimmen (mit Auto-Erkennung des OneDrive-Pfades)
      2. Pruefen, ob die Anwendung gerade geoeffnet ist (Sperrdateien)
      3. Sicherung der geschuetzten Datenbanken anlegen
      4. Programmdateien kopieren, geschuetzte Dateien ausgeschlossen
      5. Geschuetzte Datenbanken nur anlegen, falls lokal nicht vorhanden
      6. Anwendung starten

.PARAMETER Source
    Quellverzeichnis (ProgrammAA). Ohne Angabe wird es automatisch gesucht.

.PARAMETER Target
    Lokales Arbeitsverzeichnis. Standard: C:\ProgrammAA

.PARAMETER AppFile
    Zu startende Datei. Ohne Angabe wird sie im Zielverzeichnis gesucht.

.PARAMETER NoLaunch
    Nur abgleichen, Anwendung nicht starten.

.PARAMETER NoBackup
    Keine Sicherung der geschuetzten Datenbanken anlegen.

.EXAMPLE
    .\StartSupervisor.ps1

.EXAMPLE
    .\StartSupervisor.ps1 -WhatIf
#>

[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [string]$Source,
    [string]$Target = 'C:\ProgrammAA',
    [string]$AppFile,
    [switch]$NoLaunch,
    [switch]$NoBackup
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

# ---------------------------------------------------------------------------
# Konfiguration
# ---------------------------------------------------------------------------

# Diese Dateien werden NIEMALS ueberschrieben. Sie werden nur dann aus der
# Quelle uebernommen, wenn sie im Zielverzeichnis noch nicht existieren.
$ProtectedFiles = @(
    'einsatz.mdb',
    'faktbasis.mdb'
)

# Kandidaten fuer die Quelle, falls -Source nicht angegeben wurde.
$SourceCandidates = @(
    'IAAI Arbeitssicherheit GmbH\Executive Board - ProgrammSicherungen\ProgrammAA',
    'Executive Board - ProgrammSicherungen\ProgrammAA'
)

# Reihenfolge, in der die zu startende Anwendung gesucht wird.
$AppCandidates = @(
    'Supervisor.accdb',
    'Supervisor.accde',
    'Supervisor.mdb',
    'Supervisor.mde'
)

# Verzeichnis fuer die Sicherungen der geschuetzten Datenbanken.
$BackupRoot = Join-Path $Target '_Sicherung'

# Anzahl der aufzubewahrenden Sicherungsstaende je Datei.
$BackupKeep = 10

# ---------------------------------------------------------------------------
# Hilfsfunktionen
# ---------------------------------------------------------------------------

function Write-Step {
    param([string]$Text)
    Write-Host ''
    Write-Host "== $Text" -ForegroundColor Cyan
}

function Write-Ok   { param([string]$Text) Write-Host "   [ok]   $Text" -ForegroundColor Green }
function Write-Info { param([string]$Text) Write-Host "   [info] $Text" -ForegroundColor Gray }
function Write-Warn { param([string]$Text) Write-Host "   [warn] $Text" -ForegroundColor Yellow }

function Stop-WithError {
    param([string]$Text)
    Write-Host ''
    Write-Host "FEHLER: $Text" -ForegroundColor Red
    Write-Host ''
    if ($Host.Name -eq 'ConsoleHost') {
        Write-Host 'Beliebige Taste druecken zum Beenden...' -ForegroundColor DarkGray
        $null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown')
    }
    exit 1
}

function Resolve-SourcePath {
    <#
        Sucht das ProgrammAA-Verzeichnis: zuerst die konfigurierten
        Kandidatenpfade unterhalb des Benutzerprofils und aller
        OneDrive-Wurzeln, danach eine begrenzte Suche.
    #>
    param([string]$Explicit)

    if ($Explicit) {
        if (-not (Test-Path -LiteralPath $Explicit -PathType Container)) {
            Stop-WithError "Das angegebene Quellverzeichnis existiert nicht:`n$Explicit"
        }
        return (Resolve-Path -LiteralPath $Explicit).ProviderPath
    }

    $roots = New-Object System.Collections.Generic.List[string]
    $roots.Add($env:USERPROFILE)
    foreach ($name in @('OneDriveCommercial', 'OneDriveConsumer', 'OneDrive')) {
        $value = [Environment]::GetEnvironmentVariable($name)
        if ($value) { $roots.Add($value) }
    }

    $uniqueRoots = $roots | Where-Object { $_ } | Select-Object -Unique

    foreach ($root in $uniqueRoots) {
        foreach ($candidate in $SourceCandidates) {
            $path = Join-Path $root $candidate
            if (Test-Path -LiteralPath $path -PathType Container) {
                return (Resolve-Path -LiteralPath $path).ProviderPath
            }
        }
    }

    # Letzter Versuch: irgendein ProgrammAA unterhalb von ProgrammSicherungen.
    foreach ($root in $uniqueRoots) {
        $hit = Get-ChildItem -LiteralPath $root -Directory -Filter 'ProgrammAA' `
                             -Recurse -Depth 4 -ErrorAction SilentlyContinue |
               Where-Object { $_.FullName -like '*ProgrammSicherungen*' } |
               Select-Object -First 1
        if ($hit) { return $hit.FullName }
    }

    Stop-WithError @"
Das Quellverzeichnis ProgrammAA wurde nicht gefunden.
Bitte den Pfad ausdruecklich uebergeben, z. B.:

  .\StartSupervisor.ps1 -Source "C:\Users\<Benutzer>\IAAI Arbeitssicherheit GmbH\Executive Board - ProgrammSicherungen\ProgrammAA"
"@
}

function Get-ApplicationLock {
    <#
        Prueft auf Access-Sperrdateien (.ldb / .laccdb) im Zielverzeichnis.
        Ein Abgleich waehrend geoeffneter Anwendung waere nicht zuverlaessig.
    #>
    param([string]$Path)

    if (-not (Test-Path -LiteralPath $Path -PathType Container)) { return @() }

    return @(Get-ChildItem -LiteralPath $Path -File -ErrorAction SilentlyContinue |
             Where-Object { $_.Extension -in @('.ldb', '.laccdb') })
}

function Backup-ProtectedFile {
    <#
        Legt eine datierte Kopie einer geschuetzten Datenbank an und
        raeumt aeltere Staende auf.
    #>
    param([string]$FilePath)

    if (-not (Test-Path -LiteralPath $FilePath)) { return }

    $name  = [IO.Path]::GetFileNameWithoutExtension($FilePath)
    $ext   = [IO.Path]::GetExtension($FilePath)
    $stamp = Get-Date -Format 'yyyy-MM-dd_HHmmss'
    $dest  = Join-Path $BackupRoot ('{0}_{1}{2}' -f $name, $stamp, $ext)

    if (-not (Test-Path -LiteralPath $BackupRoot -PathType Container)) {
        New-Item -ItemType Directory -Path $BackupRoot -Force | Out-Null
    }

    Copy-Item -LiteralPath $FilePath -Destination $dest -Force
    Write-Ok ('Sicherung: {0}' -f (Split-Path $dest -Leaf))

    # Alte Staende aufraeumen.
    Get-ChildItem -LiteralPath $BackupRoot -File -Filter ('{0}_*{1}' -f $name, $ext) -ErrorAction SilentlyContinue |
        Sort-Object LastWriteTime -Descending |
        Select-Object -Skip $BackupKeep |
        Remove-Item -Force -ErrorAction SilentlyContinue
}

function Invoke-ProgramSync {
    <#
        Kopiert das Programmverzeichnis. Bewusst OHNE /MIR und OHNE /PURGE,
        damit lokale Zusatzdateien erhalten bleiben. Die geschuetzten
        Dateien werden ueber /XF ausgeschlossen und damit weder ueberschrieben
        noch angefasst.
    #>
    param(
        [string]$From,
        [string]$To,
        [string[]]$Exclude
    )

    $roboArgs = @(
        $From
        $To
        '/E'            # Unterverzeichnisse inkl. leerer
        '/R:2'          # 2 Wiederholungen bei Fehler
        '/W:2'          # 2 Sekunden Wartezeit
        '/NP'           # keine Fortschrittsanzeige
        '/NDL'          # keine Verzeichnisliste
        '/NJH'          # kein Job-Header
        '/NJS'          # keine Job-Zusammenfassung
        '/XD'
        $BackupRoot     # Sicherungsordner nicht anfassen
    )

    if ($Exclude -and $Exclude.Count -gt 0) {
        $roboArgs += '/XF'
        $roboArgs += $Exclude
    }

    Write-Info ('Ausgeschlossen: {0}' -f ($Exclude -join ', '))

    & robocopy.exe @roboArgs | ForEach-Object {
        $line = $_.Trim()
        if ($line) { Write-Host "          $line" -ForegroundColor DarkGray }
    }

    # Robocopy: Exitcodes 0-7 sind Erfolg, ab 8 liegt ein Fehler vor.
    $code = $LASTEXITCODE
    if ($code -ge 8) {
        Stop-WithError "Der Abgleich ist fehlgeschlagen (robocopy Exitcode $code)."
    }
}

# ---------------------------------------------------------------------------
# Hauptablauf
# ---------------------------------------------------------------------------

Write-Host ''
Write-Host '  StartSupervisor' -ForegroundColor White
Write-Host '  ---------------' -ForegroundColor DarkGray
Write-Host '  einsatz.mdb und faktbasis.mdb werden nicht ueberschrieben.' -ForegroundColor DarkGray

# --- 1. Pfade bestimmen ----------------------------------------------------

Write-Step 'Pfade bestimmen'

$Source = Resolve-SourcePath -Explicit $Source
Write-Info "Quelle: $Source"
Write-Info "Ziel:   $Target"

if (-not (Test-Path -LiteralPath $Target -PathType Container)) {
    if ($PSCmdlet.ShouldProcess($Target, 'Zielverzeichnis anlegen')) {
        New-Item -ItemType Directory -Path $Target -Force | Out-Null
        Write-Ok 'Zielverzeichnis angelegt.'
    }
}

# --- 2. Laufende Anwendung pruefen -----------------------------------------

Write-Step 'Laufende Anwendung pruefen'

$locks = Get-ApplicationLock -Path $Target
if ($locks.Count -gt 0) {
    Write-Warn 'Es wurden Access-Sperrdateien gefunden:'
    foreach ($lock in $locks) { Write-Warn "  $($lock.Name)" }
    Stop-WithError @"
Die Anwendung scheint noch geoeffnet zu sein.
Bitte zuerst alle Fenster von Supervisor / Access schliessen und
das Skript danach erneut starten.
"@
}
Write-Ok 'Keine Sperrdateien vorhanden.'

# --- 3. Geschuetzte Datenbanken sichern ------------------------------------

Write-Step 'Geschuetzte Datenbanken sichern'

$existingProtected = @()
foreach ($file in $ProtectedFiles) {
    $local = Join-Path $Target $file
    if (Test-Path -LiteralPath $local -PathType Leaf) {
        $existingProtected += $file
        $size = '{0:N1} MB' -f ((Get-Item -LiteralPath $local).Length / 1MB)
        Write-Info "$file vorhanden ($size) - wird geschuetzt"
        if (-not $NoBackup -and $PSCmdlet.ShouldProcess($local, 'Sicherung anlegen')) {
            Backup-ProtectedFile -FilePath $local
        }
    }
    else {
        Write-Info "$file lokal nicht vorhanden - wird bei Bedarf einmalig uebernommen"
    }
}

if ($existingProtected.Count -eq 0) {
    Write-Info 'Keine geschuetzten Datenbanken vorhanden (Erstinstallation).'
}

# --- 4. Programmdateien abgleichen -----------------------------------------

Write-Step 'Programmdateien abgleichen'

if ($PSCmdlet.ShouldProcess($Target, 'Programmdateien aus der Quelle kopieren')) {
    # Die geschuetzten Dateien sind grundsaetzlich ausgeschlossen. Fehlen sie
    # lokal, werden sie im naechsten Schritt gezielt und einmalig nachgezogen.
    Invoke-ProgramSync -From $Source -To $Target -Exclude $ProtectedFiles
    Write-Ok 'Programmdateien abgeglichen.'
}

# --- 5. Fehlende Datenbanken einmalig anlegen ------------------------------

Write-Step 'Datenbanken pruefen'

foreach ($file in $ProtectedFiles) {
    $local  = Join-Path $Target $file
    $remote = Join-Path $Source $file

    if (Test-Path -LiteralPath $local -PathType Leaf) {
        Write-Ok "$file unveraendert erhalten."
        continue
    }

    if (-not (Test-Path -LiteralPath $remote -PathType Leaf)) {
        Write-Warn "$file ist weder lokal noch in der Quelle vorhanden."
        continue
    }

    if ($PSCmdlet.ShouldProcess($local, 'Datenbank erstmalig aus der Quelle kopieren')) {
        Copy-Item -LiteralPath $remote -Destination $local -Force
        Write-Ok "$file erstmalig aus der Quelle uebernommen."
    }
}

# --- 6. Anwendung starten --------------------------------------------------

if ($NoLaunch) {
    Write-Step 'Fertig'
    Write-Ok 'Abgleich abgeschlossen, Start wurde uebersprungen (-NoLaunch).'
    return
}

Write-Step 'Anwendung starten'

if (-not $AppFile) {
    foreach ($candidate in $AppCandidates) {
        $path = Join-Path $Target $candidate
        if (Test-Path -LiteralPath $path -PathType Leaf) { $AppFile = $path; break }
    }
}
elseif (-not [IO.Path]::IsPathRooted($AppFile)) {
    $AppFile = Join-Path $Target $AppFile
}

if (-not $AppFile -or -not (Test-Path -LiteralPath $AppFile -PathType Leaf)) {
    Stop-WithError @"
Die zu startende Anwendung wurde im Zielverzeichnis nicht gefunden.
Gesucht wurde nach: $($AppCandidates -join ', ')

Bitte den Dateinamen ausdruecklich uebergeben, z. B.:
  .\StartSupervisor.ps1 -AppFile "Supervisor.accdb"
"@
}

Write-Info ('Datei: {0}' -f (Split-Path $AppFile -Leaf))

if ($PSCmdlet.ShouldProcess($AppFile, 'Anwendung starten')) {
    Start-Process -FilePath $AppFile -WorkingDirectory $Target
    Write-Ok 'Anwendung gestartet.'
}

Write-Host ''
