def count_animals(total_heads, total_legs):
    num_rabbits = (total_legs - 2 * total_heads) // 2
    num_chickens = total_heads - num_rabbits
    return num_chickens, num_rabbits

heads, legs = 35, 94
print(count_animals(heads, legs))