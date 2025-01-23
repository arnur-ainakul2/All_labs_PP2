# assign a multiline string to a variable:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#or with one single quotes:
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''



#Strings are Arrays
print(a)
a = "Hello, World!"
print(a[1])


#Looping Through a String
for x in "banana":
  print(x)


#String Length
a = "Hello, World!"
print(len(a))

#Check String
txt = "The best things in life are free!"
print("free" in txt) #true


txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.") #out: Yes, 'free' is present.
  
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

txt = "The best things in life are free!"
print("expensive" not in txt)
