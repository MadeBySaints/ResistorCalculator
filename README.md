# ResistorCalculator
A calculator that performs math for resistance


Calculation types:
Ohm's Law (V,I,R)
Power Calc (V,I,Ω,W)
Voltage Divider (V,Ω1,Ω2)
Series/Parallel (measures series and parallel resistances)
Resistor Color Code Decoder (input bands, and colors, and ResistanceCalculator will tell you what type of resistor it is.)

Run using the included run.bat file, or build your own executable with pyinstaller:
(png included)

@echo off
echo Installing required components...
python -m pip install --upgrade pip

echo Building executable from source code...
pyinstaller --onefile --windowed --icon=app.png --name ResistorCalculator rc.py

echo Build complete.
pause
