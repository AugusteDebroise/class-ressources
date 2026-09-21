"""
Your first Python script.

HOW TO RUN THIS FILE — two ways:

1. The Run button
   Open this file in VS Code and click the ▶ button in the top-right corner.
   The output appears in the "Terminal" panel at the bottom.

2. The terminal
   Open a terminal in VS Code (Terminal > New Terminal), then type:

       python ressources/hello_vscode.py

   (On some machines the command is `python3` instead of `python`.)

Either way, you should see the output below appear at the bottom of the screen.
Try changing something in this file, save it (Ctrl+S / Cmd+S), and run it again.
"""

# `print()` displays something on the screen.
print("Hello! You just ran a Python file.")
print()

# A variable stores a value so you can reuse it.
first_name = "Auguste"
print("This script was run by:", first_name)

# Python can do arithmetic. Try changing these numbers.
hours_per_session = 3
number_of_sessions = 8
total_hours = hours_per_session * number_of_sessions

print("Total hours of class this semester:", total_hours)
print()


# A function is a reusable block of code. It takes an input and returns a result.
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


# A loop repeats the same operation over a collection of values.
temperatures = [0, 10, 20, 30]

print("Celsius -> Fahrenheit")
for temperature in temperatures:
    converted = celsius_to_fahrenheit(temperature)
    print(temperature, "->", converted)

print()
print("It worked. You are ready for the next session.")
