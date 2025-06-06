"""
🧮 Refined Calculator
👤 Author: PJ (@pjprogrammers)
📄 License: MIT
🔗 GitHub Profile: https://github.com/pjprogrammers
🔗 GitHub Repo: https://github.com/pjprogrammers/python
Description: A sleek Tkinter calculator app that accepts both mouse clicks
and keyboard input. Supports full arithmetic expressions and respects
standard math precedence (BODMAS). Features clear, backspace, percentage,
decimal input, and smooth user interaction.
"""

import tkinter as tk
from tkinter import ttk
import re

class CalculatorApp:
    """
    Calculator app built with Tkinter.
    Supports full math expressions and keyboard input.
    Evaluates with proper math order (BODMAS).
    """

    def __init__(self, root):
        """
        Set up the calculator window, buttons, and display.
        Also bind keyboard keys to calculator functions.
        """
        self.root = root
        self.root.title("Refined Calculator")
        self.root.geometry("320x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#000000")  # Black background for sleek look

        # Store the current mathematical expression as a string
        self.expression = ''

        # Set styles for buttons and display
        self.style = ttk.Style()
        self.style.theme_use('clam')  # Modern button style

        self.style.configure('TButton', font=("Arial", 16), background="#000000", foreground="#FFFFFF", borderwidth=0)
        self.style.configure('Operation.TButton', foreground="#00FFFF", background="#000000")
        self.style.configure('Equals.TButton', foreground="#00FFFF", background="#000000")

        # Create the calculator's display and buttons
        self.create_widgets()

        # Bind keyboard inputs to the calculator
        self.root.bind("<Key>", self.on_key_press)

    def create_widgets(self):
        """
        Create the label to show expression/result and all buttons in grid.
        """
        # Label to display current expression or result, right aligned
        self.display = ttk.Label(self.root, text="0", anchor='e', font=("Arial", 40),
                                 background="#000000", foreground="#FFFFFF")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="we")

        # Button text, position, and style
        buttons = [
            ('C', 1, 0, "Operation.TButton"), ('%', 1, 1, "Operation.TButton"),
            ('⌫', 1, 2, "Operation.TButton"), ('÷', 1, 3, "Operation.TButton"),
            ('7', 2, 0, "TButton"), ('8', 2, 1, "TButton"), ('9', 2, 2, "TButton"), ('×', 2, 3, "Operation.TButton"),
            ('4', 3, 0, "TButton"), ('5', 3, 1, "TButton"), ('6', 3, 2, "TButton"), ('-', 3, 3, "Operation.TButton"),
            ('1', 4, 0, "TButton"), ('2', 4, 1, "TButton"), ('3', 4, 2, "TButton"), ('+', 4, 3, "Operation.TButton"),
            ('00', 5, 0, "TButton"), ('0', 5, 1, "TButton"), ('.', 5, 2, "TButton"), ('=', 5, 3, "Equals.TButton")
        ]

        for (text, row, col, style) in buttons:
            self.create_button(text, row, col, style)

    def create_button(self, text, row, col, style):
        """
        Create a button widget and place it on the grid.
        Clicking the button triggers the on_button_click method.
        """
        button = ttk.Button(self.root, text=text, style=style,
                            command=lambda t=text: self.on_button_click(t))
        button.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")

        # Make grid cells expandable (even though resizing is disabled)
        self.root.grid_columnconfigure(col, weight=1)
        self.root.grid_rowconfigure(row, weight=1)

    def on_button_click(self, char):
        """
        Process button clicks: digits, operators, clear, backspace, equals, percentage.
        """
        if char in '0123456789.':  # Number or decimal point
            self.append_char(char)
        elif char in '+-×÷':  # Operators
            self.append_operator(char)
        elif char == 'C':  # Clear all
            self.clear_expression()
        elif char == '⌫':  # Backspace
            self.backspace()
        elif char == '=':  # Calculate
            self.calculate()
        elif char == '%':  # Percentage
            self.calculate_percentage()

    def on_key_press(self, event):
        """
        Process keyboard input to work the calculator.
        Maps keys to calculator functions.
        """
        key = event.char
        keys_allowed = '0123456789.+-*/%'

        if key in keys_allowed:
            # Map keyboard operators to calculator symbols
            if key == '*':
                self.append_operator('×')
            elif key == '/':
                self.append_operator('÷')
            elif key == '%':
                self.calculate_percentage()
            elif key in '+-':
                self.append_operator(key)
            elif key in '0123456789.':
                self.append_char(key)
        elif event.keysym == 'Return':  # Enter key to calculate
            self.calculate()
        elif event.keysym == 'BackSpace':
            self.backspace()
        elif event.keysym == 'Escape':  # Escape key to clear
            self.clear_expression()

    def append_char(self, char):
        """
        Add a number or decimal point to the expression.
        Prevent multiple decimals in one number.
        """
        if char == '.':
            # Prevent multiple decimal points in the current number
            last_number = self.get_last_number()
            if '.' in last_number:
                return  # Ignore if decimal already exists

        self.expression += char
        self.update_display()

    def append_operator(self, operator):
        """
        Add an operator to the expression.
        Avoid two operators in a row by replacing the last one if needed.
        Allow minus at start for negative numbers.
        """
        if not self.expression:
            if operator == '-':  # Allow negative number start
                self.expression = '-'
                self.update_display()
            return

        # If last char is operator, replace it
        if self.expression[-1] in '+-×÷':
            self.expression = self.expression[:-1] + operator
        else:
            self.expression += operator

        self.update_display()

    def get_last_number(self):
        """
        Get the current number being typed, after the last operator.
        Used to prevent multiple decimal points in one number.
        """
        numbers = re.split(r'[+\-×÷]', self.expression)
        return numbers[-1] if numbers else ''

    def clear_expression(self):
        """
        Clear everything and reset display to zero.
        """
        self.expression = ''
        self.update_display()

    def backspace(self):
        """
        Remove the last character from the expression.
        """
        self.expression = self.expression[:-1]
        self.update_display()

    def calculate_percentage(self):
        """
        Convert the last number in the expression to a percentage (divide by 100).
        """
        last_number = self.get_last_number()
        if not last_number:
            return

        try:
            percent_value = str(float(last_number) / 100)
            self.expression = self.expression[:-len(last_number)] + percent_value
            self.update_display()
        except ValueError:
            pass  # Ignore if invalid number

    def calculate(self):
        """
        Evaluate the whole expression using Python's eval().
        Replace calculator symbols with Python operators first.
        Display result or error message.
        """
        if not self.expression:
            return

        expression = self.expression.replace('×', '*').replace('÷', '/')

        # Remove trailing operator if any before evaluating
        if expression[-1] in '+-*/':
            expression = expression[:-1]

        try:
            result = eval(expression)

            # Show integer if result is whole number
            if isinstance(result, float) and result.is_integer():
                result = int(result)

            self.expression = str(result)
            self.update_display()
        except Exception:
            self.expression = ''
            self.display.config(text="Error")

    def update_display(self):
        """
        Update the display label to show current expression or 0 if empty.
        """
        self.display.config(text=self.expression if self.expression else "0")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
