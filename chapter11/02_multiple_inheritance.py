class Employee():
    company="Visa"
    ecode=1608

class Freelancer():
    company="Fiverr"
    level=2

# class Programmer(Freelancer,Employee):    # if we use this then company attribue has highest priority of Freelancer class.
class Programmer(Employee,Freelancer):      # if we use this then company attribue has highest priority of Employee class.
    name="Rohit"

p=Programmer()
print(p.ecode)
print(p.level)
print(p.company)
