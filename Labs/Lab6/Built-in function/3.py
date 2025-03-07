def palindrome(word):
    b=word[::-1]
    if b==word:
        return True
    else:
        return False
slovo=str(input())
if palindrome(slovo):
    print("yes")
else:
    print("no")

