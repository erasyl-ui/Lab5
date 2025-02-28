import re

def insert_spaces_between_capitals():
    text = input("Enter a string: ")
    print(re.sub(r'(?<!^)(?=[A-Z])', ' ', text))

insert_spaces_between_capitals()
# Example: 'HelloWorldTest' -> 'Hello World Test'
