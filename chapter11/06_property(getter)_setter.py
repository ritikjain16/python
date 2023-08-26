class Employee:
    salary = 5600
    salarybonus = 500

    # using property method (getter) for changing the attributes (salarybonus)
    @property
    def totalSalary(self):
        return self.salary+self.salarybonus

    # using setter method for totalsalary
    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonus = val - self.salary


e = Employee()
print(e.totalSalary)

e.totalSalary=7000
print(e.salary)
print(e.salarybonus)
