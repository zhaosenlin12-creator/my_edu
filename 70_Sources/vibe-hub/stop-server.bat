@echo off
setlocal

set "PORT=8765"

echo === Stop VibeHub Local Mirror ===
echo.

set "FOUND=0"
for /f "tokens=5" %%P in ('netstat -ano ^| findstr ":%PORT% " ^| findstr LISTENING') do (
    echo Stopping server on PID %%P...
    taskkill /PID %%P /F
    set "FOUND=1"
)

if "%FOUND%"=="0" (
    echo No server running on port %PORT%.
)

echo.
pause