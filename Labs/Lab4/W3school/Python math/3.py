import math
a=int(input("Input number of sides "))
b=int(input("Input the length of a side "))
if a<3:
    print("It's not defined")
if a==3:
    print((math.sqrt(3)/4)*(b**2))
if a==4:
    print(a**2)
