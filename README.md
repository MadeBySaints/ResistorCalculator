# 🔧 Resistor Calculator

A comprehensive GUI-based resistor calculator and color code decoder built with Python and tkinter. Perfect for electronics enthusiasts, students, and professionals working with resistors.

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey)
![Release](https://img.shields.io/github/v/release/MadeBySaints/ResistorCalculator)
![Downloads](https://img.shields.io/github/downloads/MadeBySaints/ResistorCalculator/total)
![License](https://img.shields.io/badge/license-MIT-green)

## ✨ Features

### 🧮 Multiple Calculation Modes
- **Ohm's Law Calculator** - Calculate voltage, current, or resistance
- **Power Calculator** - Comprehensive power calculations with multiple formulas
- **Voltage Divider** - Calculate output voltage for voltage divider circuits
- **Series/Parallel Resistance** - Calculate equivalent resistance for multiple resistors
- **Color Code Decoder** - Identify resistor values from color bands

### 🎨 Color Code Decoder
- Support for **3, 4, 5, and 6-band resistors**
- **Visual color preview** for accurate band identification
- **Smart validation** prevents invalid color combinations
- Displays **resistance value, tolerance, and range**
- Includes **temperature coefficient** for 6-band resistors
- **Power rating guidance** and standard series information

### 💡 User-Friendly Interface
- Clean, intuitive GUI with tabbed interface
- Real-time input validation and error handling
- Comprehensive results with additional calculations
- Resizable window for better usability
- Clear results display with proper units

## 🚀 Quick Start

### Option 1: Download Pre-built Executable (Recommended)
1. Go to the [**Releases**](https://github.com/yourusername/ResistorCalculator/releases) page
2. Download the latest `ResistorCalculator.exe`
3. Double-click to run - **no installation required!**

### Option 2: Run from Source (Windows)
1. Download `rc.py` and `run.bat`
2. Place them in the same folder
3. Double-click `run.bat`

### Option 3: Direct Python Execution
```bash
# Clone or download the repository
git clone https://github.com/yourusername/ResistorCalculator.git
cd ResistorCalculator

# Run the calculator
python rc.py
```

### Option 4: Build Your Own Executable
1. Download the source code
2. Double-click `build.bat` to create your own EXE file

### Prerequisites (for source code only)
- Python 3.6 or higher (tkinter included)
- No additional packages required!

## 📁 Project Structure

```
ResistorCalculator/
├── rc.py              # Main application source code
├── run.bat            # Windows launcher for source code
├── build.bat          # Build script to create EXE
├── README.md          # This file
└── dist/          # Built executables
    └── ResistorCalculator.exe
```

## 📊 Calculation Examples

### Ohm's Law
- Input: **V = 5V**, **R = 1000Ω**
- Output: **I = 0.005A**, **P = 0.025W**

### Color Code (4-band example)
- Colors: **Red, Red, Brown, Gold**
- Result: **220Ω ±5%** (208Ω to 231Ω)

### Voltage Divider
- Input: **Vin = 12V**, **R1 = 1kΩ**, **R2 = 2kΩ**
- Output: **Vout = 8V**, **Ratio = 0.667**

## 🎯 Use Cases

- **Electronics Prototyping** - Calculate component values for circuits
- **Component Identification** - Decode color bands on loose resistors
- **Educational Tool** - Learn electronics principles with visual feedback
- **Circuit Design** - Plan voltage dividers and power calculations
- **Component Sorting** - Organize resistor inventory by value

## 🛠️ Technical Details

### Supported Resistor Types
| Bands | Type | Tolerance | Use Case |
|-------|------|-----------|----------|
| 3 | Carbon Composition | ±20% | General purpose |
| 4 | Standard | ±5%, ±10% | Common applications |
| 5 | Precision | ±1%, ±2% | Precision circuits |
| 6 | High Precision | ±0.1% to ±1% | High-accuracy applications |

### Calculation Formulas
- **Ohm's Law**: V = I × R, I = V / R, R = V / I
- **Power**: P = V × I, P = V² / R, P = I² × R
- **Voltage Divider**: Vout = Vin × (R2 / (R1 + R2))
- **Series**: Rtotal = R1 + R2 + R3 + ...
- **Parallel**: 1/Rtotal = 1/R1 + 1/R2 + 1/R3 + ...

## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:

- 🐛 **Report bugs** or suggest features
- 💡 **Add new calculation modes** (inductors, capacitors, etc.)
- 🎨 **Improve the UI/UX**
- 📚 **Enhance documentation**
- 🧪 **Add unit tests**

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Python's built-in **tkinter** library
- Inspired by the need for a simple, offline resistor calculator
- Color code standards based on **IEC 60062** specifications

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ for the electronics community

</div>
