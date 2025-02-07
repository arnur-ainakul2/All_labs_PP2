def find_primes():
    values = map(int, input("Enter numbers: ").split())

    def is_prime(n):
        if n < 2:
            return False
        for divisor in range(2, int(n**0.5) + 1):
            if n % divisor == 0:
                return False
        return True

    print("Prime numbers:", [num for num in values if is_prime(num)])

find_primes()