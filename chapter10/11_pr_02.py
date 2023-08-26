class Calculator:
    def __init__(self,num):
        self.num=num

    def square(self):
        print(f"The suare of {self.num} is {self.num **2}")   #    **2 gives square 

    def squareRoot(self):
        print(f"The suare root of {self.num} is {self.num **(1/2)}")

    def cube(self):
        print(f"The cube of {self.num} is {self.num **3}")

n=Calculator(4)
n.square()
n.squareRoot()
n.cube()