@echo off
REM Build script for Resistor Calculator EXE with auto-incrementing version
REM This script will create a standalone executable using PyInstaller

title Resistor Calculator Builder

echo =========================================
echo    Resistor Calculator EXE Builder
echo =========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo Python found! Checking version...
python --version
echo.

REM Read current version from version.txt, or start at 0.1.1 if file doesn't exist
set "version_file=version.txt"
if not exist "%version_file%" (
    echo 0.1.1 > "%version_file%"
    set "current_version=0.1.1"
) else (
    set /p current_version=<"%version_file%"
)

echo Current version: %current_version%

REM Parse version components (assumes format: major.minor.patch)
for /f "tokens=1,2,3 delims=." %%a in ("%current_version%") do (
    set "major=%%a"
    set "minor=%%b"
    set "patch=%%c"
)

REM Increment patch version
set /a patch+=1

REM Create new version string
set "new_version=%major%.%minor%.%patch%"

echo New version: %new_version%
echo %new_version% > "%version_file%"

echo.
echo Installing required components...
python -m pip install --upgrade pip
python -m pip install pyinstaller

echo.
echo Building executable from source code...
echo Target: ResistorCalculator-v%new_version%.exe
echo.

REM Build with version in filename
pyinstaller --onefile --windowed --icon=app.png --name "ResistorCalculator-v%new_version%" rc.py

if %errorlevel% equ 0 (
    echo.
    echo =========================================
    echo Build completed successfully!
    echo Version: %new_version%
    echo Output: dist\ResistorCalculator-v%new_version%.exe
    echo =========================================
    echo.
    
    REM Optional: Copy to releases folder
    if not exist "releases" mkdir releases
    copy "dist\ResistorCalculator-v%new_version%.exe" "releases\" >nul
    if %errorlevel% equ 0 (
        echo File copied to releases folder.
    )
    
) else (
    echo.
    echo =========================================
    echo Build failed!
    echo Reverting version number...
    echo =========================================
    set /a patch-=1
    set "reverted_version=%major%.%minor%.%patch%"
    echo %reverted_version% > "%version_file%"
    echo Version reverted to: %reverted_version%
)

echo.
pause