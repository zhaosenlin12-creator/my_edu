@echo off
setlocal

set "PORT=8765"
set "VAULT=C:\my_know"
set "SITE_DIR=%VAULT%\70_Sources\vibe-hub\site"

echo === VibeHub Local Mirror ===
echo.
echo Site directory: %SITE_DIR%
echo Port: %PORT%
echo.

REM Stop any existing server on this port
for /f "tokens=5" %%P in ('netstat -ano ^| findstr ":%PORT% " ^| findstr LISTENING') do (
    echo Stopping existing server on PID %%P...
    taskkill /PID %%P /F >nul 2>&1
)

REM Verify python is available
where python >nul 2>&1
if errorlevel 1 (
    echo ERROR: python not found in PATH
    pause
    exit /b 1
)

if not exist "%SITE_DIR%\index.html" (
    echo ERROR: Site directory not found: %SITE_DIR%
    echo Run the mirror script first.
    pause
    exit /b 1
)

echo Starting server...
echo Open http://localhost:%PORT%/ in your browser.
echo Close this window or press Ctrl+C to stop.
echo.

REM Start server in a new window so user can keep this one open
start "VibeHub Mirror (port %PORT%)" /MIN python -m http.server %PORT% --directory "%SITE_DIR%"

REM Give server a moment, then open browser
timeout /t 2 /nobreak >nul
start http://localhost:%PORT%/

echo.
echo Server running in background. Use stop-server.bat to shut down.
echo.
pause