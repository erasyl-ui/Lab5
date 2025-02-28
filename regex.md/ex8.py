import re

def split_at_uppercase():
    text = input("Enter a string: ")
    print(re.findall(r'[A-Z][^A-Z]*', text))

split_at_uppercase()
# Example: 'HelloWorldTest' -> ['Hello', 'World', 'Test']
