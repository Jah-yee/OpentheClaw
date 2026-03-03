@echo off
set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%\.."
python "launcher\openclaw_launcher.py" webui


