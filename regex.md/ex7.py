import re

def snake_to_camel():
    text = input("Enter a snake_case string: ")
    words = text.split('_')
    print(words[0] + ''.join(word.capitalize() for word in words[1:]))

snake_to_camel()
# Example: 'hello_world_test' -> 'helloWorldTest'
