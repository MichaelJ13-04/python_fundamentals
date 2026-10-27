# Author: Michael Moody
# Program: String Manipulation
# Purpose: Transform text, count words, and find palindromes.
The program validates text input and handles empty input.

"""
Program: String Manipulation
Purpose: Transform and analyze user-provided text.
Demonstrates uppercase conversion, reversal, word counting,
and palindrome detection with input validation.
"""

# Ask the user for valid text.
while True:
    text = input("Enter a sentence (1-200 characters): ").strip()

    if not text:
        print("Input cannot be empty. Please try again.")
    elif len(text) > 200:
        print("Please enter no more than 200 characters.")
    else:
        break

# Transformation: change case and reverse the text.
print("Uppercase:", text.upper())
print("Reversed:", text[::-1])

# Analysis: split the sentence into words.
words = text.split()

print("Word count:", len(words))
print("First four words:", words[:4])

# Remove common punctuation and convert words to lowercase.
cleaned_words = [
    word.strip(".,!?;:'\"()[]{}").lower()
    for word in words
]

# Find words that read the same forward and backward.
palindromes = [
    word for word in cleaned_words
    if len(word) > 1 and word == word[::-1]
]

print("Palindromes found:", palindromes)

