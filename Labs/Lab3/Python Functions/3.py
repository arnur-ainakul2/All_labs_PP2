""" Return values """
def functi(x):
    return 5**x
print(functi(3))
print(functi(4))
print(functi(9))

#Pass statement
"""
function definitions cannot be empty,
but if you for some reason have a function definition with no content, put in the pass 
statement to avoid getting an error.
"""
def funk():
    pass


#Positional-Only Arguments
def my_func(x, /):
    print(x)
my_func(3)

def my2(x):
    print(x)
my2(x=3)

#Keyword-Only Arguments
def my_func(*, x):
    print(x)
my_func(x=3)
#Without the *, you are allowed to use positionale arguments even if the function expects keyword arguments:
def my_func2(x):
    print(x)
my_func2(2)

#Combine Positional-Only and Keyword-Only
def my2(a,b, /, *,c,d):
    print(a+b+c+d)
my2(5,6,c=7,d=8)


