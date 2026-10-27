#Author:Michael Moody
# Program: Circle Area Calculator
# Purpose: Calculate the area of a circle using its radius.
The program validates input and retries if the input is invalid.

"""
Program: Circle Area Calculator
Purpose: Calculate the area of a circle using its radius.
Includes input validation and exception handling.
"""

import math

# Ask the user for a valid radius.
while True:
    try:
        radius = float(input("Enter the circle's radius: ").strip())

        # Reject infinity and NaN.
        if not math.isfinite(radius):
            print("Invalid input. Please enter a finite number.")
            continue

        # A radius cannot be negative.
        if radius < 0:
            print("Radius cannot be negative. Please try again.")
            continue

        break

    except ValueError:
        print("Invalid input. Enter a number, such as 5 or 2.5.")

# Calculate the area using pi * radius squared.
area = math.pi * radius ** 2

# Display the result to two decimal places.
print(f"The area of the circle is {area:.2f} square units.")

