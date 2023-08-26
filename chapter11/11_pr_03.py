class Employee:
    salary=100
    increment=1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary + self.increment
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,inc):
        self.increment=inc/self.salary


e=Employee()
print(e.salaryAfterIncrement)

e.salaryAfterIncrement=200
print(e.increment)