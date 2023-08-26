class Person():
    country="India"

    def takeBreath(self):
        print("I am Breathing..")



class Employee(Person):
    company="Honda"

    def getSalary(self,salary):
     print("Salary is 2000")

    
    def takeBreath(self):
        print("I am Breathing and i am an employee")



class Programmer(Employee):
    company="Fiverr"

    def getSalary(self):
        print("No salary to Programmers.")


p=Person()
e=Employee()
pr=Programmer()

# if an object uses an attribute or method which is not in respective class then it takes that from nearest Parent.

print(p.country)
p.takeBreath()


print(e.country)
e.takeBreath()
print(e.company)



print(pr.country)
pr.takeBreath()
print(pr.company)
