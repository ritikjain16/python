class Programmer():
    company="Microsoft"
    def __init__(self,name,product):
        self.name =name
        self.product=product
    def printDetails(self):
        print(f"The name of {self.company} programmer is {self.name} and working on product {self.product}.")


Ritik=Programmer("Ritik","Github")
Pragati=Programmer("Pragati","Skype")

Ritik.printDetails()
Pragati.printDetails()