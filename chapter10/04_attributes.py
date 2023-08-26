# class attributes - which are define inside the class
class Employee():
    company = "Google" # class attributes

e1=Employee()
print(e1.company) # if not given any value to e1.company

# e1.company="YouTube"  # we can change the value for our object at any time
# print(e1.company)


# instance attributes - not define inside the class , define in main program.

e1.salary=2000
print(e1.salary)




# we can change the value of class attributes for all
Employee.company="Microsoft"
print(e1.company)
