# Author: Michael Moody
# python_fundamentals
A collection of beginner Python programs and exercises.
Python Fundamentals 

Project Description 

This repository contains beginner Python programs demonstrating numeric input validation, exception handling, calculations, and string manipulation. 

Requirements 

Python 3.x 

No third-party packages are required. 

Program 1: Circle Area Calculator 

File: circle_area.py 

Purpose: Calculates the area of a circle using the formula: 

Area = pi * radius² 

How to run: 

bash 

python circle_area.py 
 

If your system uses the python3 command, run: 

bash 

python3 circle_area.py 
 

Input handling and assumptions: 

The radius must be a finite number. 

Negative radii are rejected. 

Invalid numeric input prompts the user to try again. 

A radius of zero is allowed. 

The result is displayed to two decimal places. 

The area is expressed in square units because no measurement unit is specified. 

Program 2: String Manipulation 

File: string_manipulation.py 

Purpose: Demonstrates text transformation and analysis. 

Operations performed: 

Converts text to uppercase. 

Reverses the text. 

Counts the words. 

Displays the first four words. 

Identifies palindromes after removing common punctuation. 

How to run: 

bash 

python string_manipulation.py 
 

Or use python3 if required by your system. 

Input handling and assumptions: 

Leading and trailing whitespace is removed. 

Empty input is rejected. 

Input must contain between 1 and 200 characters after trimming. 

Words are separated by whitespace. 

Palindrome matching is case-insensitive and ignores the listed punctuation at word boundaries. 

Testing Evidence 

Run each test manually and record the observed result before submitting. 

Circle Area Calculator 

Test input 

Expected behavior 

5 

Displays an area of approximately 78.54 

2.5 

Accepts decimal input and displays approximately 19.63 

hello 

Displays an error and asks for input again 

-3 

Rejects the negative radius and asks again 

0 

Displays an area of 0.00 

nan or inf 

Rejects the non-finite value and asks again 

String Manipulation 

Test input 

Expected behavior 

Racecar and kayak 

Identifies racecar and kayak as palindromes 

Empty input or spaces only 

Displays an error and asks again 

Text longer than 200 characters 

Displays an error and asks again 

Hello World 

Displays uppercase text, reversed text, and a word count of 2 

Edge cases tested: After performing the tests above, document at least one actual edge case you tested, the input you used, and the observed result. For example, enter -3 in the circle calculator and confirm that it rejects the radius and prompts again. 

Project Structure 

text 

python_fundamentals/ 
├── README.md 
├── circle_area.py 
└── string_manipulation.py 
 

Notes 

Each Python script runs independently. No additional files or external libraries are required. 

 
