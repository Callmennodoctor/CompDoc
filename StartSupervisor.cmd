@echo off
rem ---------------------------------------------------------------------------
rem  StartSupervisor - Starter zum Doppelklicken
rem
rem  Ruft StartSupervisor.ps1 aus demselben Verzeichnis auf. Die Ausfuehrungs-
rem  richtlinie wird nur fuer diesen einen Aufruf gelockert, es wird nichts
rem  dauerhaft am System veraendert.
rem
rem  Zusaetzliche Parameter werden durchgereicht, z. B.:
rem     StartSupervisor.cmd -WhatIf
rem     StartSupervisor.cmd -NoLaunch
rem ---------------------------------------------------------------------------

setlocal
set "SCRIPT=%~dp0StartSupervisor.ps1"

if not exist "%SCRIPT%" (
    echo FEHLER: StartSupervisor.ps1 wurde nicht gefunden neben dieser Datei.
    echo Erwartet: "%SCRIPT%"
    pause
    exit /b 1
)

powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%SCRIPT%" %*
set "RC=%ERRORLEVEL%"

if not "%RC%"=="0" (
    echo.
    echo Das Skript wurde mit Fehlercode %RC% beendet.
    pause
)

endlocal & exit /b %RC%
