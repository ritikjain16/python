class Employee():
    company="Camel"
    salary=100
    location="Delhi"

    # def changeSalary(self,sal):
    #     self.salary=sal




    # for changing the class salary attribute 
     
    # def changeSalary(self,sal):
    #     self.__class__.salary=sal

    #OR

    @classmethod     # self is replace by cls
    def changeSalary(cls,sal):
        cls.salary=sal


e=Employee()

print(e.salary)
print(Employee.salary)
e.changeSalary(455)
print(e.salary)
print(Employee.salary)