import re

def replace_chars(text):
    pattern = r"[ ,.]"  # Matches space, comma, or dot
    return re.sub(pattern, ":", text)

text = input("Enter a string: ")
print("Modified string:", replace_chars(text))