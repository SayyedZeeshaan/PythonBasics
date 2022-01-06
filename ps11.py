
# Single Inheritance


class Employee:                                       # base class or parent class
    company = "Ezygen"                   

    def showDetails(self):
        print("This is an employee")

class Programmer (Employee):                           # derived class or child class
    language = "Python"

    def getlanguage(self):
        print(f"The language is {self.language}")

    def showDetails(self):             # this is used to over ride the base class 
        print("This is a programmer")  # If this function is absent then it takes from base class

e = Employee()
p = Programmer()
e.showDetails()
p.showDetails()
# p can use all functions in e but e cannot use all functions of p 
print(e.company)
print(p.company)  #  --> company is not defined in child class so it takes it from (parent / base) class 
# e.getlanguage()    --> this throws error because there is no such function in the base class
p.getlanguage()                  


#  Multiple Inheritance

class Employee:
    company = "Ezygen"

class Trainee:
    company = "Infosys"

class Programmer(Employee , Trainee):
    name = "zeeshaan"

p = Programmer()
print(p.company)  # Gives priority to the Class first mentioned in child/derived class
  # if trainee was written first in child/derived class then output would have been infosys

  

# Multi-Level Inheritance

class Person:
    country = "India"

    def playing(self):
        print(f"Playing for a team all day ")

    def getSalary(self):
        print(f"Salary is 100k")

class Employee(Person):
    company = "Ezygen"
    
    def getSalary(self):
        print(f"Salary is 500k")
    
    def playing(self):
        print(f"Gets very little time to play")

class Programmer(Employee):
    company = "Google"

    def getSalary(self):
        print(f"Salary is 1000k")

    def playing(self):
        super().playing()     # super() first parent class function then child class function
        print(f"Gets no time to play")

p = Person()
e = Employee()
pr = Programmer()


print(pr.company)   # --> even if not defined takes from employee and if not in employee then from person
print(e.company)
# print(p.company) --> throws error because company not defined


print(p.country)
print(pr.country)   
print(e.country)

p.getSalary()
e.getSalary()
pr.getSalary()

p.playing()                
e.playing()
pr.playing()   # prints if present in programmer class if not present takes from employee class and if not present takes from person class

                

class Employee:
    company = "Asus"
    salary = 500000
    location = "Akola"

    @classmethod
    def changeSalary(cls,sal):  # class method used to change class and not object of class 
        cls.salary = sal

e = Employee()
print(e.salary)
e.changeSalary(200000)
print(e.salary)



