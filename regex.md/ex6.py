import re

def replace_space_comma_dot():
    text = input("Enter a string: ")
    print(re.sub(r'[ ,.]', ':', text))

replace_space_comma_dot()
# Example: 'Hello, world. This is a test' -> 'Hello:world:This:is:a:test'
