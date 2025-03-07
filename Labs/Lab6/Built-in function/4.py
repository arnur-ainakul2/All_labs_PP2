import time
import math
a=int(input("input number:"))
c=math.sqrt(a)
b=float(input("time:"))
time.sleep(b / 1000)
print(f"Square root of {a} after {b} miliseconds is {c}")
