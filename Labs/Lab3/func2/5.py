def contains_consecutive_threes(sequence):
    return any(sequence[index] == sequence[index + 1] == 3 for index in range(len(sequence) - 1))

print(contains_consecutive_threes([1, 3, 3]))  # True
print(contains_consecutive_threes([1, 3, 1, 3]))  # False
print(contains_consecutive_threes([3, 1, 3]))  # False