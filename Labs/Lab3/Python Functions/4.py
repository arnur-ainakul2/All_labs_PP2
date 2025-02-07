#Recursion
"""
Python also accepts function recursion,
which means a defined function can call itself.
"""
def tri_recursion(x):
    if(x>0):
        result=x+tri_recursion(x-1)
        print(result)
    else:
        result=0
        return result
print("Recursion Example Results:")
tri_recursion(6)