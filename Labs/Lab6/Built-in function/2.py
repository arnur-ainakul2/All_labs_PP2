def uppercase(stri):
    if stri.isupper():
        return 1
    else:
        return 0
def lowercase(stri):
    if stri.islower():
        return 1
    else:
        return 0
stri=str(input())
uppers=0
lowers=0
for i in range(len(stri)):
    uppers+=uppercase(stri[i])
for i in range(len(stri)):
    lowers+=lowercase(stri[i])
print(f"number of upper-case letters {uppers}\nnumber of lower-case letters {lowers}")
    

    
    


