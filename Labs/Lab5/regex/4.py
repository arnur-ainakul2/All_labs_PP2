import re

def text_match(text):
    pattern = r"[A-Z][a-z]+"  
    if re.search(pattern, text):
        return "Found a match!"
    else:
        return "Not matched!"

b = input("Enter a string: ")
print(text_match(b))