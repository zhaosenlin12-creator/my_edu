@echo off
setlocal

call "%~dp0stop-server.bat"
echo.
call "%~dp0start-server.bat"