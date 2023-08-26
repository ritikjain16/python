class Employee:
    company="Google"

    # making an constructor
    def __init__(self):
        print("Employee is created.")

    # making an constructor with arguments
    def __init__(self,id,code):
        self.id=id
        self.code=code
        print("Employee is created.")
    
    def printDetails(self):
        print(f"id is {self.id}")
        print(f"code is {self.code}")


    def name(self):
        print(f"Hello sir,Your salary is {self.salary} in {self.company}")

    # making a static method  -- not take self
    @staticmethod
    def greet():
        print(f"Hello sir ")
    
    @staticmethod
    def wish():
        print("Good Morning")




# we only make an object but constructer method auto generates.
e1=Employee(32,1608)  # we give arguments inside class as we make a constructor.
e1.printDetails()

# e1 = Employee()
# e1.wish()

# e1.salary=2050
# e1.name()