class Employee():
    company="Google"
    # def name():   # wrong bcz always throws an error bcz we have to give 'self' inside name method.
    def name(self):
        print(f"Hello sir,Your salary is {self.salary} in {self.company}")  # always use fstring

e1=Employee()
e1.salary=10000
e1.name() 
# Employee.name(e1)



# IMPORTANT NOTE:
# e1.name or Employee.name(e1) is same , it means it required 1 arguments , so we give 'self' argument.


