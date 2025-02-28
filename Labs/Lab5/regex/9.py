import re

def add_spaces(s):
    return re.sub(r'(?<!^)([A-Z])', r' \1', s)

# Example usage
s = input("Enter a string: ")
print(add_spaces(s))