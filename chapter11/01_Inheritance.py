# inheritance - way of creating a class from an existing class

class Employee():
    company="Google"

    def showDetails(self):
        print("This is an employee")



class programmer(Employee):    # programmer inherits Employee class
    language="python"

    def getLanguage(self):
        print(f"language is {self.language}")

    def showDetails(self):
        print("This is a Programmer")




p=programmer()
print(p.company)  # we can use attributes and methods of employee class without making the method in programmer class.

p.company="Microsoft"   # but we can change the value for our requirement.
print(p.company)

p.showDetails()


# e=Employee()
# e.getLanguage()     # AttributeError: 'Employee' object has no function 'getLanguage'



# but if we have same method in both class then it will prefer in which the method is declared.
p.showDetails()