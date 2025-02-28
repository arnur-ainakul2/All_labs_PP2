import re

def text_match(text):
    pattern = r"^ab{2,3}$"  
    if re.search(pattern, text):
        return "Found a match!"
    else:
        return "Not matched!"

b = input("Enter a string: ")
print(text_match(b))