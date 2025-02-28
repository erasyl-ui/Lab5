import re

def match_a_anything_b():
    text = input("Enter a string: ")
    print(bool(re.fullmatch(r'a.*b', text)))

match_a_anything_b()
# Example: 'acb', 'ab', 'a123b' -> True; 'abc', 'b' -> False
