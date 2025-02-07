def to_celsius(fahrenheit_temp):
    return (5 / 9) * (fahrenheit_temp - 32)

fahrenheit_value = int(input("Enter temperature in Fahrenheit: "))
print("Celsius: ", to_celsius(fahrenheit_value))