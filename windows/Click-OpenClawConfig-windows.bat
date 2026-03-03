@echo off
setlocal
set "SCRIPT_DIR=%~dp0"
set "ROOT_DIR=%SCRIPT_DIR%..\"
pushd "%ROOT_DIR%"
echo Opening OpenClaw config in browser...
python "launcher\openclaw_launcher.py" config
if errorlevel 1 (
  py "launcher\openclaw_launcher.py" config
)
if errorlevel 1 (
  echo.
  echo Failed. Install Python 3 from python.org and ensure it is in PATH (or use the "py" launcher).
)
pause
popd
endlocal
