import re

def match_a_followed_by_two_to_three_b():
    text = input("Enter a string: ")
    print(bool(re.fullmatch(r'ab{2,3}', text)))

match_a_followed_by_two_to_three_b()
# Example: 'abb', 'abbb' -> True; 'ab', 'abbbb' -> False
