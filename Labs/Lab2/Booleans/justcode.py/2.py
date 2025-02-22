class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.secondname=lname
    def printname(self):
        print(self.firstname,self.secondname)
class Student(Person):
    def __init__(self,fname,lname,year):  #When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
        super().__init__(fname,lname)
        self.graduateyare=year
    def welcome(self):
        print("Welcome",self.firstname,self.secondname,"to the class of", self.graduateyare)
x=Student("Mike","Lake",2019)
x.welcome()