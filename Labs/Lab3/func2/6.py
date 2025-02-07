def detect_sequence(numbers):
    return [0, 0, 7] in [numbers[idx:idx+3] for idx in range(len(numbers) - 2)]

sequence = list(map(int, input("Введите числа через пробел: ").split()))
print(detect_sequence(sequence))
