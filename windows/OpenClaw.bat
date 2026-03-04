@echo off
setlocal
set "ROOT=%~dp0..\"
pushd "%ROOT%"
echo Starting OpenClaw Web UI...
python launch.py
if errorlevel 1 py launch.py
if errorlevel 1 (
  echo.
  echo Failed. Install Python 3 from python.org and ensure it is in PATH (or use the "py" launcher).
)
pause
popd
endlocal
