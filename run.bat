@echo off
REM Resistor Calculator Launcher
REM This script will start the Resistor Calculator GUI application

title Resistor Calculator Launcher

echo =========================================
echo    Resistor Calculator Launcher
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

REM Check if the resistor calculator script exists
if not exist "rc.py" (
    echo.
    echo ERROR: rc.py not found in current directory
    echo Please make sure the Python script is in the same folder as this batch file
    echo Current directory: %CD%
    echo.
    pause
    exit /b 1
)

echo Script found: rc.py
echo.

REM Check for required modules (tkinter should be included with Python)
echo Checking for required modules...
python -c "import tkinter; import math" >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Required modules not found
    echo tkinter and math modules are required
    echo These should be included with standard Python installation
    echo.
    pause
    exit /b 1
)

echo All modules available!
echo.
echo Starting Resistor Calculator...
echo.

REM Start the calculator and close terminal immediately
echo Launching Resistor Calculator...
start "" pythonw rc.py

REM Exit immediately - terminal will close
exit