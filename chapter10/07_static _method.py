class Employee:
    company="Google"
    def name(self):
        print(f"Hello sir,Your salary is {self.salary} in {self.company}")

    # making a static method  -- not take self
    @staticmethod
    def greet():
        print(f"Hello sir ")
    
    @staticmethod
    def wish():
        print("Good Morning")


e1=Employee()

e1.greet()
e1.wish()
