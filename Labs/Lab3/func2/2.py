def identify_primes():
    input_numbers = map(int, input("Введите числа через пробел: ").split())

    def is_prime(number):
        if number < 2:
            return False
        for divisor in range(2, int(number**0.5) + 1):
            if number % divisor == 0:
                return False
        return True

    prime_numbers = [value for value in input_numbers if is_prime(value)]
    print("Простые числа:", prime_numbers)

identify_primes()