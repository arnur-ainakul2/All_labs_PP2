import re

def split_at_uppercase(s):
    return re.findall('[A-Z][^A-Z]*', s)

# Example usage
s = input("Enter a string: ")
print(split_at_uppercase(s))