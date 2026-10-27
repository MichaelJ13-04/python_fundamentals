# Author: Michael Moody
# Program: String Manipulation
# Purpose: Transform text, count words, and find palindromes.
The program validates text input and handles empty input.
"""

while True:
    text = input("Enter a sentence (1-200 characters): ").strip()

    if not text:
        print("Input cannot be empty. Please try again.")
    elif len(text) > 200:
        print("Please enter no more than 200 characters.")
    else:
        break

# Transformation: reverse the text and change its case.
print("Uppercase:", text.upper())
print("Reversed:", text[::-1])

# Analysis: count words and display the first four.
words = text.split()
print("Word count:", len(words))
print("First four words:", words[:4])

# Remove common punctuation before identifying palindromes.
cleaned_words = [
    word.strip(".,!?;:'\"()[]{}").lower()
    for word in words
]

palindromes = [
    word for word in cleaned_words
    if len(word) > 1 and word == word[::-1]
]

print("Palindromes found:", palindromes)
