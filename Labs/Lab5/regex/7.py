import re

def snake_to_camel(snake_str):
    components = snake_str.split('_')  
    return components[0] + ''.join(word.capitalize() for word in components[1:])  # Capitalize each word except the first

snake_str = input("Enter a snake_case string: ")
print("CamelCase:", snake_to_camel(snake_str))