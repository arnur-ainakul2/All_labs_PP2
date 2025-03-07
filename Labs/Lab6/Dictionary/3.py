import os

path = input("Enter the file path: ")

if os.path.exists(path):
    print(f"Path '{path}' exists.")
    print(f"Directory: {os.path.dirname(path)}")
    print(f"Filename: {os.path.basename(path)}")
else:
    print(f"Path '{path}' does not exist.")