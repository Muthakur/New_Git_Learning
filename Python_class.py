# python class
class student:
    roll=1                              #static variable 
    def __init__(self,name,age):        #constructor
        print("constructor is created")
        self.name=name                  #instant variable 
        self.age=age

    def show(self):
        print("My name is :",self.name)
        print("My age is :",self.age)



s=student("Mukesh",1)
s.show()             #accesing using object
print(s.name)        #By object
print(student.roll)  #accesing static variable using class name 

#s1=student("Raj",2)  
