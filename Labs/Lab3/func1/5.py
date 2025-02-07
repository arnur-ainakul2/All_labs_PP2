from itertools import permutations

def generate_permutations():
    user_input = input("Enter something: ")
    for perm in permutations(user_input):
        print("".join(perm))

generate_permutations()