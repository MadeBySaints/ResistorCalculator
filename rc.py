import tkinter as tk
from tkinter import ttk, messagebox
import math

class ResistorCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Resistor Calculator")
        self.root.geometry("500x650")
        self.root.resizable(True, True)
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="Resistor Calculator", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Calculator type selection
        calc_frame = ttk.LabelFrame(main_frame, text="Calculation Type", padding="10")
        calc_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        calc_frame.columnconfigure(1, weight=1)
        
        self.calc_type = tk.StringVar(value="ohms_law")
        
        ttk.Radiobutton(calc_frame, text="Ohm's Law (V, I, R)", 
                       variable=self.calc_type, value="ohms_law",
                       command=self.update_interface).grid(row=0, column=0, sticky=tk.W)
        
        ttk.Radiobutton(calc_frame, text="Power Calculations", 
                       variable=self.calc_type, value="power",
                       command=self.update_interface).grid(row=0, column=1, sticky=tk.W)
        
        ttk.Radiobutton(calc_frame, text="Voltage Divider", 
                       variable=self.calc_type, value="voltage_divider",
                       command=self.update_interface).grid(row=0, column=2, sticky=tk.W)
        
        ttk.Radiobutton(calc_frame, text="Series/Parallel", 
                       variable=self.calc_type, value="series_parallel",
                       command=self.update_interface).grid(row=1, column=0, sticky=tk.W)
        
        ttk.Radiobutton(calc_frame, text="Color Code Decoder", 
                       variable=self.calc_type, value="color_code",
                       command=self.update_interface).grid(row=1, column=1, sticky=tk.W)
        
        ttk.Radiobutton(calc_frame, text="Reverse Lookup", 
                       variable=self.calc_type, value="reverse_lookup",
                       command=self.update_interface).grid(row=1, column=2, sticky=tk.W)
        
        # Input frame
        self.input_frame = ttk.LabelFrame(main_frame, text="Input Values", padding="10")
        self.input_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        self.input_frame.columnconfigure(1, weight=1)
        
        # Result frame
        result_frame = ttk.LabelFrame(main_frame, text="Results", padding="10")
        result_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        result_frame.columnconfigure(0, weight=1)
        
        self.result_text = tk.Text(result_frame, height=8, width=50, wrap=tk.WORD)
        scrollbar = ttk.Scrollbar(result_frame, orient=tk.VERTICAL, command=self.result_text.yview)
        self.result_text.configure(yscrollcommand=scrollbar.set)
        
        self.result_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        result_frame.rowconfigure(0, weight=1)
        
        # Calculate button
        self.calc_button = ttk.Button(main_frame, text="Calculate", 
                                     command=self.calculate, style="Accent.TButton")
        self.calc_button.grid(row=4, column=0, columnspan=3, pady=10)
        
        # Clear button
        clear_button = ttk.Button(main_frame, text="Clear Results", 
                                 command=self.clear_results)
        clear_button.grid(row=5, column=0, columnspan=3, pady=(0, 10))
        
        # Initialize interface
        self.update_interface()
    
    def clear_widgets(self, frame):
        """Clear all widgets from a frame"""
        for widget in frame.winfo_children():
            widget.destroy()
    
    def update_interface(self):
        """Update the input interface based on selected calculation type"""
        self.clear_widgets(self.input_frame)
        calc_type = self.calc_type.get()
        
        if calc_type == "ohms_law":
            self.setup_ohms_law_interface()
        elif calc_type == "power":
            self.setup_power_interface()
        elif calc_type == "voltage_divider":
            self.setup_voltage_divider_interface()
        elif calc_type == "series_parallel":
            self.setup_series_parallel_interface()
        elif calc_type == "color_code":
            self.setup_color_code_interface()
        elif calc_type == "reverse_lookup":
            self.setup_reverse_lookup_interface()
    
    def setup_ohms_law_interface(self):
        """Setup interface for Ohm's law calculations"""
        ttk.Label(self.input_frame, text="Enter any two values (leave one empty):").grid(
            row=0, column=0, columnspan=2, sticky=tk.W, pady=(0, 10))
        
        ttk.Label(self.input_frame, text="Voltage (V):").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.voltage_var = tk.StringVar()
        ttk.Entry(self.input_frame, textvariable=self.voltage_var).grid(
            row=1, column=1, sticky=(tk.W, tk.E), pady=2, padx=(10, 0))
        
        ttk.Label(self.input_frame, text="Current (A):").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.current_var = tk.StringVar()
        ttk.Entry(self.input_frame, textvariable=self.current_var).grid(
            row=2, column=1, sticky=(tk.W, tk.E), pady=2, padx=(10, 0))
        
        ttk.Label(self.input_frame, text="Resistance (Ω):").grid(row=3, column=0, sticky=tk.W, pady=2)
        self.resistance_var = tk.StringVar()
        ttk.Entry(self.input_frame, textvariable=self.resistance_var).grid(
            row=3, column=1, sticky=(tk.W, tk.E), pady=2, padx=(10, 0))
    
    def setup_power_interface(self):
        """Setup interface for power calculations"""
        ttk.Label(self.input_frame, text="Enter any two values:").grid(
            row=0, column=0, columnspan=2, sticky=tk.W, pady=(0, 10))
        
        ttk.Label(self.input_frame, text="Voltage (V):").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.voltage_var = tk.StringVar()
        ttk.Entry(self.input_frame, textvariable=self.voltage_var).grid(
            row=1, column=1, sticky=(tk.W, tk.E), pady=2, padx=(10, 0))
        
        ttk.Label(self.input_frame, text="Current (A):").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.current_var = tk.StringVar()
        ttk.Entry(self.input_frame, textvariable=self.current_var).grid(
            row=2, column=1, sticky=(tk.W, tk.E), pady=2, padx=(10, 0))
        
        ttk.Label(self.input_frame, text="Resistance (Ω):").grid(row=3, column=0, sticky=tk.W, pady=2)
        self.resistance_var = tk.StringVar()
        ttk.Entry(self.input_frame, textvariable=self.resistance_var).grid(
            row=3, column=1, sticky=(tk.W, tk.E), pady=2, padx=(10, 0))
        
        ttk.Label(self.input_frame, text="Power (W):").grid(row=4, column=0, sticky=tk.W, pady=2)
        self.power_var = tk.StringVar()
        ttk.Entry(self.input_frame, textvariable=self.power_var).grid(
            row=4, column=1, sticky=(tk.W, tk.E), pady=2, padx=(10, 0))
    
    def setup_voltage_divider_interface(self):
        """Setup interface for voltage divider calculations"""
        ttk.Label(self.input_frame, text="Voltage Divider Calculator:").grid(
            row=0, column=0, columnspan=2, sticky=tk.W, pady=(0, 10))
        
        ttk.Label(self.input_frame, text="Input Voltage (V):").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.input_voltage_var = tk.StringVar()
        ttk.Entry(self.input_frame, textvariable=self.input_voltage_var).grid(
            row=1, column=1, sticky=(tk.W, tk.E), pady=2, padx=(10, 0))
        
        ttk.Label(self.input_frame, text="R1 (Ω):").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.r1_var = tk.StringVar()
        ttk.Entry(self.input_frame, textvariable=self.r1_var).grid(
            row=2, column=1, sticky=(tk.W, tk.E), pady=2, padx=(10, 0))
        
        ttk.Label(self.input_frame, text="R2 (Ω):").grid(row=3, column=0, sticky=tk.W, pady=2)
        self.r2_var = tk.StringVar()
        ttk.Entry(self.input_frame, textvariable=self.r2_var).grid(
            row=3, column=1, sticky=(tk.W, tk.E), pady=2, padx=(10, 0))
    
    def setup_series_parallel_interface(self):
        """Setup interface for series/parallel resistance calculations"""
        ttk.Label(self.input_frame, text="Resistor Values (comma-separated):").grid(
            row=0, column=0, columnspan=2, sticky=tk.W, pady=(0, 5))
        
        ttk.Label(self.input_frame, text="Resistors (Ω):").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.resistors_var = tk.StringVar()
        ttk.Entry(self.input_frame, textvariable=self.resistors_var).grid(
            row=1, column=1, sticky=(tk.W, tk.E), pady=2, padx=(10, 0))
        
        ttk.Label(self.input_frame, text="Example: 100, 200, 330").grid(
            row=2, column=1, sticky=tk.W, pady=(0, 10), padx=(10, 0))
    
    def setup_reverse_lookup_interface(self):
        """Setup interface for reverse lookup (resistance to color bands)"""
        ttk.Label(self.input_frame, text="Find Color Bands for Resistance Value:").grid(
            row=0, column=0, columnspan=2, sticky=tk.W, pady=(0, 10))
        
        ttk.Label(self.input_frame, text="Resistance (Ω):").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.lookup_resistance_var = tk.StringVar()
        ttk.Entry(self.input_frame, textvariable=self.lookup_resistance_var).grid(
            row=1, column=1, sticky=(tk.W, tk.E), pady=2, padx=(10, 0))
        
        ttk.Label(self.input_frame, text="Examples: 330, 1000, 4.7k, 2.2M").grid(
            row=2, column=1, sticky=tk.W, pady=(0, 5), padx=(10, 0))
        
        ttk.Label(self.input_frame, text="Number of Bands:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.lookup_bands_var = tk.StringVar(value="4")
        bands_combo = ttk.Combobox(self.input_frame, textvariable=self.lookup_bands_var, 
                                  values=["3", "4", "5", "6"], state="readonly", width=5)
        bands_combo.grid(row=3, column=1, sticky=tk.W, padx=(10, 0), pady=5)
        
        # Tolerance selection for 4, 5, and 6 band resistors
        ttk.Label(self.input_frame, text="Tolerance (%):").grid(row=4, column=0, sticky=tk.W, pady=2)
        self.lookup_tolerance_var = tk.StringVar(value="5")
        tolerance_combo = ttk.Combobox(self.input_frame, textvariable=self.lookup_tolerance_var,
                                     values=["0.05", "0.1", "0.25", "0.5", "1", "2", "5", "10", "20"], 
                                     state="readonly", width=10)
        tolerance_combo.grid(row=4, column=1, sticky=tk.W, padx=(10, 0), pady=2)
    
    def setup_color_code_interface(self):
        """Setup interface for resistor color code decoding"""
        # Color code mapping
        self.color_values = {
            'Black': 0, 'Brown': 1, 'Red': 2, 'Orange': 3, 'Yellow': 4,
            'Green': 5, 'Blue': 6, 'Violet': 7, 'Gray': 8, 'White': 9,
            'Gold': -1, 'Silver': -2
        }
        
        self.tolerance_values = {
            'Brown': 1, 'Red': 2, 'Gold': 5, 'Silver': 10,
            'Green': 0.5, 'Blue': 0.25, 'Violet': 0.1, 'Gray': 0.05
        }
        
        self.temp_coefficient = {
            'Brown': 100, 'Red': 50, 'Orange': 15, 'Yellow': 25,
            'Blue': 10, 'Violet': 5
        }
        
        # Number of bands selection
        ttk.Label(self.input_frame, text="Number of Bands:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.bands_var = tk.StringVar(value="4")
        bands_combo = ttk.Combobox(self.input_frame, textvariable=self.bands_var, 
                                  values=["3", "4", "5", "6"], state="readonly", width=5)
        bands_combo.grid(row=0, column=1, sticky=tk.W, padx=(10, 0), pady=5)
        bands_combo.bind('<<ComboboxSelected>>', self.update_color_bands)
        
        # Resistor type info
        self.type_label = ttk.Label(self.input_frame, text="", foreground="blue")
        self.type_label.grid(row=0, column=2, sticky=tk.W, padx=(20, 0), pady=5)
        
        # Color selection frame
        self.color_frame = ttk.Frame(self.input_frame)
        self.color_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        
        # Initialize color band interface
        self.update_color_bands()
    
    def update_color_bands(self, event=None):
        """Update color band selection based on number of bands"""
        # Clear existing widgets
        for widget in self.color_frame.winfo_children():
            widget.destroy()
        
        num_bands = int(self.bands_var.get())
        
        # Update resistor type label
        type_info = {
            3: "Carbon Composition (±20%)",
            4: "Standard Resistor (±5% or ±10%)",
            5: "Precision Resistor (±1% or ±2%)",
            6: "High Precision (±0.1% to ±1%)"
        }
        self.type_label.config(text=type_info[num_bands])
        
        # Color options
        standard_colors = ['Black', 'Brown', 'Red', 'Orange', 'Yellow', 
                          'Green', 'Blue', 'Violet', 'Gray', 'White']
        multiplier_colors = standard_colors + ['Gold', 'Silver']
        tolerance_colors = ['Brown', 'Red', 'Gold', 'Silver', 'Green', 'Blue', 'Violet', 'Gray']
        temp_coeff_colors = ['Brown', 'Red', 'Orange', 'Yellow', 'Blue', 'Violet']
        
        # Create color selection widgets
        self.color_vars = []
        
        # Band labels
        band_labels = []
        if num_bands == 3:
            band_labels = ["1st Digit", "2nd Digit", "Multiplier"]
        elif num_bands == 4:
            band_labels = ["1st Digit", "2nd Digit", "Multiplier", "Tolerance"]
        elif num_bands == 5:
            band_labels = ["1st Digit", "2nd Digit", "3rd Digit", "Multiplier", "Tolerance"]
        elif num_bands == 6:
            band_labels = ["1st Digit", "2nd Digit", "3rd Digit", "Multiplier", "Tolerance", "Temp Coeff"]
        
        for i, label in enumerate(band_labels):
            # Label
            ttk.Label(self.color_frame, text=f"{label}:").grid(row=i, column=0, sticky=tk.W, pady=2)
            
            # Color selection
            color_var = tk.StringVar()
            self.color_vars.append(color_var)
            
            # Determine available colors for this band
            if i < len(band_labels) - 2:  # Digit bands
                if i == 0 and num_bands > 3:  # First digit can't be black (except 3-band)
                    colors = standard_colors[1:]  # Exclude black
                else:
                    colors = standard_colors
            elif label == "Multiplier":
                colors = multiplier_colors
            elif label == "Tolerance":
                colors = tolerance_colors
            elif label == "Temp Coeff":
                colors = temp_coeff_colors
            else:
                colors = standard_colors
            
            combo = ttk.Combobox(self.color_frame, textvariable=color_var, 
                               values=colors, state="readonly", width=10)
            combo.grid(row=i, column=1, sticky=tk.W, padx=(10, 0), pady=2)
            
            # Color preview
            color_canvas = tk.Canvas(self.color_frame, width=30, height=20, bg="white", relief=tk.SUNKEN)
            color_canvas.grid(row=i, column=2, padx=(10, 0), pady=2)
            
            # Bind color change to update preview
            combo.bind('<<ComboboxSelected>>', lambda e, canvas=color_canvas, var=color_var: 
                      self.update_color_preview(canvas, var.get()))
    
    def calculate(self):
        """Perform calculation based on selected type"""
        try:
            calc_type = self.calc_type.get()
            
            if calc_type == "ohms_law":
                self.calculate_ohms_law()
            elif calc_type == "power":
                self.calculate_power()
            elif calc_type == "voltage_divider":
                self.calculate_voltage_divider()
            elif calc_type == "series_parallel":
                self.calculate_series_parallel()
            elif calc_type == "color_code":
                self.calculate_color_code()
            elif calc_type == "reverse_lookup":
                self.calculate_reverse_lookup()
                
        except Exception as e:
            messagebox.showerror("Error", f"Calculation error: {str(e)}")
    
    def parse_resistance_value(self, value_str):
        """Parse resistance value with k/M suffixes"""
        value_str = value_str.strip().upper()
        
        if value_str.endswith('K'):
            return float(value_str[:-1]) * 1000
        elif value_str.endswith('M'):
            return float(value_str[:-1]) * 1000000
        else:
            return float(value_str)
    
    def calculate_reverse_lookup(self):
        """Calculate color bands for given resistance value"""
        resistance_str = self.lookup_resistance_var.get().strip()
        if not resistance_str:
            raise ValueError("Please enter a resistance value")
        
        resistance = self.parse_resistance_value(resistance_str)
        num_bands = int(self.lookup_bands_var.get())
        tolerance = float(self.lookup_tolerance_var.get())
        
        result = "=== Reverse Lookup: Resistance to Color Bands ===\n\n"
        result += f"Target Resistance: {self.format_resistance(resistance)}\n"
        result += f"Number of Bands: {num_bands}\n"
        result += f"Tolerance: ±{tolerance}%\n\n"
        
        # Color mappings (reverse of decode)
        value_to_color = {v: k for k, v in {
            'Black': 0, 'Brown': 1, 'Red': 2, 'Orange': 3, 'Yellow': 4,
            'Green': 5, 'Blue': 6, 'Violet': 7, 'Gray': 8, 'White': 9
        }.items()}
        
        tolerance_to_color = {v: k for k, v in {
            'Brown': 1, 'Red': 2, 'Gold': 5, 'Silver': 10,
            'Green': 0.5, 'Blue': 0.25, 'Violet': 0.1, 'Gray': 0.05
        }.items()}
        
        # Find the best representation
        colors = self.find_color_bands(resistance, num_bands, tolerance, 
                                     value_to_color, tolerance_to_color)
        
        if colors:
            result += f"Color Bands: {' - '.join(colors)}\n\n"
            
            # Show band meanings
            band_labels = []
            if num_bands == 3:
                band_labels = ["1st Digit", "2nd Digit", "Multiplier"]
            elif num_bands == 4:
                band_labels = ["1st Digit", "2nd Digit", "Multiplier", "Tolerance"]
            elif num_bands == 5:
                band_labels = ["1st Digit", "2nd Digit", "3rd Digit", "Multiplier", "Tolerance"]
            elif num_bands == 6:
                band_labels = ["1st Digit", "2nd Digit", "3rd Digit", "Multiplier", "Tolerance", "Temp Coeff"]
            
            result += "Band Breakdown:\n"
            for i, (label, color) in enumerate(zip(band_labels, colors)):
                result += f"• {label}: {color}\n"
            
            # Verify the result
            calculated_resistance = self.verify_color_combination(colors, num_bands)
            result += f"\nVerification: {self.format_resistance(calculated_resistance)}\n"
            
            if abs(calculated_resistance - resistance) / resistance < 0.001:
                result += "✓ Exact match!\n"
            else:
                error_percent = abs(calculated_resistance - resistance) / resistance * 100
                result += f"Approximation error: {error_percent:.2f}%\n"
        else:
            result += "Could not find exact color band representation.\n"
            result += "This value may not be available in standard resistor series.\n\n"
            
            # Suggest nearest standard values
            standard_values = self.get_standard_values_near(resistance)
            result += "Nearest standard values:\n"
            for val in standard_values:
                result += f"• {self.format_resistance(val)}\n"
        
        self.display_result(result)
    
    def find_color_bands(self, resistance, num_bands, tolerance, value_to_color, tolerance_to_color):
        """Find color bands for given resistance value"""
        # Try to find the best multiplier and significant digits
        log_resistance = math.log10(resistance)
        
        if num_bands == 3:
            # 2 significant digits
            if log_resistance < 2:  # Less than 100 ohms
                return None  # 3-band resistors typically start at 100 ohms
            
            multiplier_power = int(log_resistance) - 1
            significant_part = resistance / (10 ** multiplier_power)
            
            if significant_part >= 100:
                multiplier_power += 1
                significant_part = resistance / (10 ** multiplier_power)
            
            digit1 = int(significant_part // 10)
            digit2 = int(significant_part % 10)
            
            if digit1 in value_to_color and digit2 in value_to_color and multiplier_power in value_to_color:
                return [value_to_color[digit1], value_to_color[digit2], value_to_color[multiplier_power]]
        
        elif num_bands in [4, 5, 6]:
            # Determine number of significant digits
            sig_digits = 2 if num_bands == 4 else 3
            
            # Find the best multiplier
            multiplier_power = max(-2, int(log_resistance) - sig_digits + 1)
            significant_part = resistance / (10 ** multiplier_power)
            
            # Adjust if necessary
            max_significant = 10 ** sig_digits
            if significant_part >= max_significant:
                multiplier_power += 1
                significant_part = resistance / (10 ** multiplier_power)
            
            # Round to nearest integer
            significant_part = round(significant_part)
            
            if sig_digits == 2:
                if significant_part < 10 or significant_part >= 100:
                    return None
                digit1 = significant_part // 10
                digit2 = significant_part % 10
                digits = [digit1, digit2]
            else:  # sig_digits == 3
                if significant_part < 100 or significant_part >= 1000:
                    return None
                digit1 = significant_part // 100
                digit2 = (significant_part // 10) % 10
                digit3 = significant_part % 10
                digits = [digit1, digit2, digit3]
            
            # Check if all digits are valid colors
            if not all(d in value_to_color for d in digits):
                return None
            
            # Check if multiplier is valid
            if multiplier_power not in value_to_color:
                return None
            
            colors = [value_to_color[d] for d in digits] + [value_to_color[multiplier_power]]
            
            # Add tolerance
            if tolerance in tolerance_to_color:
                colors.append(tolerance_to_color[tolerance])
            else:
                colors.append('Gold')  # Default to 5% if exact tolerance not found
            
            # Add temperature coefficient for 6-band (default Brown = 100ppm)
            if num_bands == 6:
                colors.append('Brown')
            
            return colors
        
        return None
    
    def verify_color_combination(self, colors, num_bands):
        """Verify what resistance value the color combination produces"""
        color_values = {
            'Black': 0, 'Brown': 1, 'Red': 2, 'Orange': 3, 'Yellow': 4,
            'Green': 5, 'Blue': 6, 'Violet': 7, 'Gray': 8, 'White': 9,
            'Gold': -1, 'Silver': -2
        }
        
        if num_bands == 3:
            digit1 = color_values[colors[0]]
            digit2 = color_values[colors[1]]
            multiplier = color_values[colors[2]]
            return (digit1 * 10 + digit2) * (10 ** multiplier)
        
        elif num_bands == 4:
            digit1 = color_values[colors[0]]
            digit2 = color_values[colors[1]]
            multiplier = color_values[colors[2]]
            return (digit1 * 10 + digit2) * (10 ** multiplier)
        
        elif num_bands in [5, 6]:
            digit1 = color_values[colors[0]]
            digit2 = color_values[colors[1]]
            digit3 = color_values[colors[2]]
            multiplier = color_values[colors[3]]
            return (digit1 * 100 + digit2 * 10 + digit3) * (10 ** multiplier)
        
        return 0
    
    def get_standard_values_near(self, target_resistance):
        """Get standard resistor values near the target"""
        # E12 series (common 5% and 10% resistors)
        e12_base = [1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]
        
        # Find the appropriate decade
        log_target = math.log10(target_resistance)
        decade_power = int(log_target)
        decade_multiplier = 10 ** decade_power
        
        # Generate values in the target decade and adjacent decades
        standard_values = []
        for power in [decade_power - 1, decade_power, decade_power + 1]:
            multiplier = 10 ** power
            for base in e12_base:
                value = base * multiplier
                if value > 0.1:  # Minimum practical resistor value
                    standard_values.append(value)
        
        # Sort by difference from target
        standard_values.sort(key=lambda x: abs(x - target_resistance))
    
    def calculate_ohms_law(self):
        """Calculate using Ohm's law"""
        v = self.get_float_value(self.voltage_var.get())
        i = self.get_float_value(self.current_var.get())
        r = self.get_float_value(self.resistance_var.get())
        
        values_entered = sum(x is not None for x in [v, i, r])
        
        if values_entered != 2:
            raise ValueError("Please enter exactly two values")
        
        result = "=== Ohm's Law Calculation ===\n\n"
        
        if v is None:  # Calculate voltage
            v = i * r
            result += f"Given: I = {i} A, R = {r} Ω\n"
            result += f"Voltage (V = I × R) = {v:.6f} V\n"
        elif i is None:  # Calculate current
            i = v / r
            result += f"Given: V = {v} V, R = {r} Ω\n"
            result += f"Current (I = V / R) = {i:.6f} A\n"
        elif r is None:  # Calculate resistance
            r = v / i
            result += f"Given: V = {v} V, I = {i} A\n"
            result += f"Resistance (R = V / I) = {r:.6f} Ω\n"
        
        # Add power calculation
        power = v * i
        result += f"\nAdditional Info:\n"
        result += f"Power (P = V × I) = {power:.6f} W\n"
        
        self.display_result(result)
    
    def update_color_preview(self, canvas, color_name):
        """Update color preview canvas"""
        color_map = {
            'Black': '#000000', 'Brown': '#8B4513', 'Red': '#FF0000',
            'Orange': '#FFA500', 'Yellow': '#FFFF00', 'Green': '#008000',
            'Blue': '#0000FF', 'Violet': '#8B00FF', 'Gray': '#808080',
            'White': '#FFFFFF', 'Gold': '#FFD700', 'Silver': '#C0C0C0'
        }
        
        if color_name in color_map:
            canvas.delete("all")
            canvas.create_rectangle(2, 2, 28, 18, fill=color_map[color_name], 
                                  outline="black", width=1)
    
    def calculate_color_code(self):
        """Decode resistor color code"""
        num_bands = int(self.bands_var.get())
        
        # Check if all required colors are selected
        for i, var in enumerate(self.color_vars):
            if not var.get():
                raise ValueError(f"Please select color for band {i+1}")
        
        colors = [var.get() for var in self.color_vars]
        
        result = "=== Resistor Color Code Decoder ===\n\n"
        result += f"Number of bands: {num_bands}\n"
        result += f"Colors: {' - '.join(colors)}\n\n"
        
        # Calculate resistance value
        if num_bands == 3:
            # 3-band: digit1, digit2, multiplier
            digit1 = self.color_values[colors[0]]
            digit2 = self.color_values[colors[1]]
            multiplier = self.color_values[colors[2]]
            
            resistance = (digit1 * 10 + digit2) * (10 ** multiplier)
            tolerance = 20  # Default for 3-band resistors
            
        elif num_bands == 4:
            # 4-band: digit1, digit2, multiplier, tolerance
            digit1 = self.color_values[colors[0]]
            digit2 = self.color_values[colors[1]]
            multiplier = self.color_values[colors[2]]
            tolerance = self.tolerance_values.get(colors[3], 0)
            
            resistance = (digit1 * 10 + digit2) * (10 ** multiplier)
            
        elif num_bands == 5:
            # 5-band: digit1, digit2, digit3, multiplier, tolerance
            digit1 = self.color_values[colors[0]]
            digit2 = self.color_values[colors[1]]
            digit3 = self.color_values[colors[2]]
            multiplier = self.color_values[colors[3]]
            tolerance = self.tolerance_values.get(colors[4], 0)
            
            resistance = (digit1 * 100 + digit2 * 10 + digit3) * (10 ** multiplier)
            
        elif num_bands == 6:
            # 6-band: digit1, digit2, digit3, multiplier, tolerance, temp_coeff
            digit1 = self.color_values[colors[0]]
            digit2 = self.color_values[colors[1]]
            digit3 = self.color_values[colors[2]]
            multiplier = self.color_values[colors[3]]
            tolerance = self.tolerance_values.get(colors[4], 0)
            temp_coeff = self.temp_coefficient.get(colors[5], 0)
            
            resistance = (digit1 * 100 + digit2 * 10 + digit3) * (10 ** multiplier)
        
        # Format resistance value
        formatted_resistance = self.format_resistance(resistance)
        
        result += f"Resistance: {formatted_resistance}\n"
        result += f"Tolerance: ±{tolerance}%\n"
        
        if num_bands == 6:
            result += f"Temperature Coefficient: {temp_coeff} ppm/°C\n"
        
        # Add resistance range
        min_resistance = resistance * (1 - tolerance/100)
        max_resistance = resistance * (1 + tolerance/100)
        result += f"\nResistance Range:\n"
        result += f"Minimum: {self.format_resistance(min_resistance)}\n"
        result += f"Maximum: {self.format_resistance(max_resistance)}\n"
        
        # Add power rating info
        result += f"\nCommon Power Ratings:\n"
        result += f"• 1/8 W (0.125 W) - Small resistors\n"
        result += f"• 1/4 W (0.25 W) - Standard resistors\n"
        result += f"• 1/2 W (0.5 W) - Medium resistors\n"
        result += f"• 1 W and above - Power resistors\n"
        
        # Add standard series info
        result += f"\nStandard Series:\n"
        if tolerance == 20:
            result += f"• E6 series (20% tolerance)\n"
        elif tolerance in [10, 5]:
            result += f"• E12 series (10% tolerance) or E24 series (5% tolerance)\n"
        elif tolerance in [2, 1]:
            result += f"• E48 series (2% tolerance) or E96 series (1% tolerance)\n"
        else:
            result += f"• High precision series\n"
        
        self.display_result(result)
    
    def format_resistance(self, resistance):
        """Format resistance value with appropriate units"""
        if resistance >= 1_000_000:
            return f"{resistance/1_000_000:.2f} MΩ"
        elif resistance >= 1_000:
            return f"{resistance/1_000:.2f} kΩ"
        else:
            return f"{resistance:.2f} Ω"
    
    def calculate_power(self):
        """Calculate power and missing values"""
        v = self.get_float_value(self.voltage_var.get())
        i = self.get_float_value(self.current_var.get())
        r = self.get_float_value(self.resistance_var.get())
        p = self.get_float_value(self.power_var.get())
        
        values = [v, i, r, p]
        non_none_values = [x for x in values if x is not None]
        
        if len(non_none_values) < 2:
            raise ValueError("Please enter at least two values")
        
        result = "=== Power Calculation ===\n\n"
        
        # Calculate missing values using available combinations
        if v is not None and i is not None:
            if r is None: r = v / i
            if p is None: p = v * i
        elif v is not None and r is not None:
            if i is None: i = v / r
            if p is None: p = (v ** 2) / r
        elif v is not None and p is not None:
            if i is None: i = p / v
            if r is None: r = (v ** 2) / p
        elif i is not None and r is not None:
            if v is None: v = i * r
            if p is None: p = (i ** 2) * r
        elif i is not None and p is not None:
            if v is None: v = p / i
            if r is None: r = p / (i ** 2)
        elif r is not None and p is not None:
            if v is None: v = math.sqrt(p * r)
            if i is None: i = math.sqrt(p / r)
        
        result += f"Results:\n"
        result += f"Voltage (V) = {v:.6f} V\n"
        result += f"Current (I) = {i:.6f} A\n"
        result += f"Resistance (R) = {r:.6f} Ω\n"
        result += f"Power (P) = {p:.6f} W\n"
        
        self.display_result(result)
    
    def calculate_voltage_divider(self):
        """Calculate voltage divider output"""
        vin = self.get_float_value(self.input_voltage_var.get())
        r1 = self.get_float_value(self.r1_var.get())
        r2 = self.get_float_value(self.r2_var.get())
        
        if None in [vin, r1, r2]:
            raise ValueError("Please enter all values for voltage divider")
        
        vout = (r2 / (r1 + r2)) * vin
        current = vin / (r1 + r2)
        
        result = "=== Voltage Divider Calculation ===\n\n"
        result += f"Input Voltage: {vin} V\n"
        result += f"R1: {r1} Ω\n"
        result += f"R2: {r2} Ω\n\n"
        result += f"Output Voltage: {vout:.6f} V\n"
        result += f"Total Current: {current:.6f} A\n"
        result += f"Voltage Ratio: {vout/vin:.4f}\n"
        
        self.display_result(result)
    
    def calculate_series_parallel(self):
        """Calculate series and parallel resistance"""
        resistors_str = self.resistors_var.get().strip()
        
        if not resistors_str:
            raise ValueError("Please enter resistor values")
        
        try:
            resistors = [float(x.strip()) for x in resistors_str.split(',')]
        except ValueError:
            raise ValueError("Invalid resistor values. Use numbers separated by commas")
        
        if len(resistors) < 2:
            raise ValueError("Please enter at least 2 resistor values")
        
        # Series resistance
        r_series = sum(resistors)
        
        # Parallel resistance
        r_parallel = 1 / sum(1/r for r in resistors)
        
        result = "=== Series/Parallel Resistance ===\n\n"
        result += f"Resistor values: {', '.join(f'{r} Ω' for r in resistors)}\n\n"
        result += f"Series Resistance: {r_series:.6f} Ω\n"
        result += f"Parallel Resistance: {r_parallel:.6f} Ω\n\n"
        
        # Show individual parallel calculations for reference
        result += "Parallel calculation: 1/Rtotal = "
        result += " + ".join(f"1/{r}" for r in resistors) + "\n"
        
        self.display_result(result)
    
    def get_float_value(self, value_str):
        """Convert string to float, return None if empty or invalid"""
        if not value_str or not value_str.strip():
            return None
        try:
            return float(value_str.strip())
        except ValueError:
            raise ValueError(f"Invalid number: '{value_str}'")
    
    def display_result(self, result):
        """Display result in the text widget"""
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(1.0, result)
    
    def clear_results(self):
        """Clear the results text widget"""
        self.result_text.delete(1.0, tk.END)

def main():
    root = tk.Tk()
    app = ResistorCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()