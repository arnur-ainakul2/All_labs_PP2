import re

def text_match(text):
    pattern = r"^a.*b$"  
    if re.fullmatch(pattern, text):
        return "Found a match!"
    else:
        return "Not matched!"

b = input("Enter a string: ")
print(text_match(b))
