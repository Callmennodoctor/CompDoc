# CompDoc

## StartSupervisor

Neubau von `StartSupervisor.exe` als Skript.

Der Launcher gleicht das lokale Arbeitsverzeichnis mit der Ablage `ProgrammAA`
ab und startet anschliessend die Supervisor-Anwendung.

**Kernaenderung:** `einsatz.mdb` und `faktbasis.mdb` werden beim Abgleich nicht
mehr ueberschrieben. Sie sind vom Kopiervorgang ausgeschlossen und werden nur
dann aus der Quelle uebernommen, wenn sie lokal noch gar nicht existieren
(Erstinstallation).

### Dateien

| Datei                 | Zweck                                       |
| --------------------- | ------------------------------------------- |
| `StartSupervisor.ps1` | Der eigentliche Launcher                    |
| `StartSupervisor.cmd` | Starter zum Doppelklicken, ruft das PS1 auf |

### Verwendung

Doppelklick auf `StartSupervisor.cmd`, oder aus der PowerShell:

```powershell
# Normaler Start
.\StartSupervisor.ps1

# Trockenlauf, es wird nichts geschrieben
.\StartSupervisor.ps1 -WhatIf

# Nur abgleichen, ohne die Anwendung zu starten
.\StartSupervisor.ps1 -NoLaunch

# Pfade ausdruecklich vorgeben
.\StartSupervisor.ps1 -Source "C:\Users\<Benutzer>\IAAI Arbeitssicherheit GmbH\Executive Board - ProgrammSicherungen\ProgrammAA" -Target "C:\ProgrammAA"
```

### Parameter

| Parameter   | Standard        | Bedeutung                                            |
| ----------- | --------------- | ---------------------------------------------------- |
| `-Source`   | Auto-Erkennung  | Quellverzeichnis `ProgrammAA` im OneDrive            |
| `-Target`   | `C:\ProgrammAA` | Lokales Arbeitsverzeichnis                           |
| `-AppFile`  | Auto-Erkennung  | Zu startende Datei, z. B. `Supervisor.accdb`         |
| `-NoLaunch` | aus             | Nur abgleichen, nicht starten                        |
| `-NoBackup` | aus             | Keine Sicherung der geschuetzten Datenbanken anlegen |
| `-WhatIf`   | aus             | Trockenlauf                                          |

### Ablauf

1. **Pfade bestimmen** – `ProgrammAA` wird unterhalb des Benutzerprofils und
   der OneDrive-Wurzeln gesucht, falls `-Source` fehlt.
2. **Sperrdateien pruefen** – liegt eine `.ldb` oder `.laccdb` im Ziel, bricht
   das Skript ab, damit nicht in eine geoeffnete Anwendung hinein kopiert wird.
3. **Sicherung** – von `einsatz.mdb` und `faktbasis.mdb` wird eine datierte
   Kopie unter `_Sicherung` abgelegt, die letzten 10 Staende bleiben erhalten.
4. **Abgleich** – `robocopy /E` ohne `/MIR` und ohne `/PURGE`, damit lokale
   Zusatzdateien bestehen bleiben. Die geschuetzten Datenbanken sind ueber
   `/XF` ausgeschlossen.
5. **Datenbanken pruefen** – fehlt eine geschuetzte Datenbank lokal, wird sie
   einmalig aus der Quelle kopiert. Ist sie vorhanden, bleibt sie unangetastet.
6. **Start** – die Anwendung wird mit dem Zielverzeichnis als Arbeitsverzeichnis
   gestartet.

### Anpassen

Die geschuetzten Dateien stehen im Konfigurationsblock oben in
`StartSupervisor.ps1`:

```powershell
$ProtectedFiles = @(
    'einsatz.mdb',
    'faktbasis.mdb'
)
```

Weitere Dateien lassen sich dort einfach ergaenzen. Ebenso die Kandidaten fuer
die zu startende Datei (`$AppCandidates`), falls die Anwendung anders heisst.
