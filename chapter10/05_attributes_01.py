# instance attributes have high preference always than class attributes.


class Employee():
    name="Ritik"
    salary="15000"


# if we have class attribute value and not instance attribute then we get class attribute value.
e1=Employee()
print(e1.name)
print(e1.salary)

# if we give instance attribute value , we get instance attribute value(higher preference).
e1.name="Pragati"
e1.salary=25000
print(e1.name)
print(e1.salary)

# print(e1.address) # throws an error (no address attribute of Employee)
