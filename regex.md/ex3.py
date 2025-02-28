import re

def find_lowercase_underscore():
    text = input("Enter a string: ")
    print(re.findall(r'\b[a-z]+_[a-z]+\b', text))

find_lowercase_underscore()
# Example: 'hello_world', 'test_example' -> ['hello_world', 'test_example']
