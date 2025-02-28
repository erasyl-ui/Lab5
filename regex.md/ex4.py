import re

def find_uppercase_followed_by_lowercase():
    text = input("Enter a string: ")
    print(re.findall(r'\b[A-Z][a-z]+\b', text))

find_uppercase_followed_by_lowercase()
# Example: 'Hello', 'Test', 'Example' -> ['Hello', 'Test', 'Example']
