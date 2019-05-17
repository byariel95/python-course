class Person:
    name = ""
    last_name = ""
    age = 0
    country = ""

    def __init__(self,name,last_name,age,country):
        self.name = name 
        self.last_name = last_name
        self.age = age
        self.country = country


    def my_name(self):
        print("My full name is",self.name,self.last_name)
        self.my_dates()

    def my_dates(self):
        print("I'm",self.age,"years old","and I'm from",self.country) 

class Employee:
    job ="builder"
    
#multiple herency 
class Student(Person,Employee):
     school = "" 

student = Student("jose","laparra",25,"Guatemala")

print(student.name,student.last_name,"and my job is",student.job)
student.my_name()

