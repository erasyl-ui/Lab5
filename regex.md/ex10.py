import re

def camel_to_snake():
    text = input("Enter a camelCase string: ")
    print(re.sub(r'([a-z])([A-Z])', r'\1_\2', text).lower())

camel_to_snake()
# Example: 'helloWorldTest' -> 'hello_world_test'
