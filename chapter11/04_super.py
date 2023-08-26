class Person():
    country="India"

    def __init__(self):
        super().__init__()      # super calls person
        print("Initialising Person...")

    def takeBreath(self):
        print("I am Breathing..")



class Employee(Person):
    company="Honda"

    def __init__(self):
        super().__init__()            # super first calls person then employee
        print("Initialising Employee")

    def getSalary(self):
        print("Salary is 2000")

    
    def takeBreath(self):
        print("I am Breathing and i am an employee")



class Programmer(Employee):
    company="Fiverr"

    def __init__(self):
        super().__init__()
        print("Initialising Programmer")   # super first calls person then employee and then Programmer

    def getSalary(self):
        print("No salary to Programmers.")


p=Person()
e=Employee()
pr=Programmer()


pr.getSalary()