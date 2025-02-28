import re

def match_a_followed_by_b():
    text = input("Enter a string: ")
    print(bool(re.fullmatch(r'ab*', text)))

match_a_followed_by_b()
# Example: 'ab', 'a', 'abb' -> True; 'b', 'ba' -> False
