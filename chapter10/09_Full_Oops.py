class Employee():
    company="Google"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        print("Employee is created!")
    
    def printDetails(self):
        print(f"Your name is {self.name}")
        print(f"Your salary is {self.salary}")
        print(f"Your company is {self.company}")
        print(f"Your number is {self.num}")

    @staticmethod
    def greet():
        print("Hello Sir!")


e1=Employee("Ritik",25000)
e1.greet()
e1.num=25
e1.printDetails()
