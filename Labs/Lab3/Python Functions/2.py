def my_function(*kids):
    print("the best child is"+kids[1])
my_function("email","tovias","dsdsa")

def func(ch1,ch2,ch3):
    print("the best child is "+ ch3)
func(ch1="d23",ch2="233",ch3="gdsf")

def func(ch1,ch2,ch3):
    print("the best child is "+ ch2)
func(ch1="d23",ch2="233",ch3="gdsf")

def my_f(**kid):
    print("His last name is s"+ kid["lname"])
my_f(fname="ttttt", lname="result")

def f(country="Norway"):
    print("I am from "+ country)
f("Sweden")
f("India")
f()
f("Brazil")


def my_rr(fog):
    for x in fog:
        print(x)

fruits=["apple","banana","cherry"]
my_rr(fruits)




