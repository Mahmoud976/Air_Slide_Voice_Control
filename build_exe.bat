@echo off
setlocal
cd /d "%~dp0"

echo ============================================
echo       AirSlide Voice Control - EXE Build
echo ============================================
echo.

if not exist ".venv\Scripts\python.exe" (
    echo [1/3] Creating virtual environment...
    py -m venv .venv
    if errorlevel 1 goto :error
)

echo [2/3] Installing dependencies...
".venv\Scripts\python.exe" -m pip install --upgrade pip
if errorlevel 1 goto :error
".venv\Scripts\python.exe" -m pip install -r requirements.txt pyinstaller
if errorlevel 1 goto :error

echo [3/3] Packaging executable...
".venv\Scripts\python.exe" -m PyInstaller --noconfirm --clean --onefile --name AirSlideVoiceControl --collect-all vosk --collect-all sounddevice --collect-all cffi --hidden-import vosk --hidden-import sounddevice voice_control.py
if errorlevel 1 goto :error

echo.
echo Build complete: dist\AirSlideVoiceControl.exe
echo IMPORTANT: Copy the Vosk model folders you need beside the EXE.
pause
exit /b 0

:error
echo.
echo Build failed. Review the error messages above.
pause
exit /b 1
