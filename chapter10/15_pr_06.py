class Attributes():
    a=3
    def change(self):
        print(f"value is {self.a}")

  # we can change the 'self' argument to any 'argument' but for simplicity we always use 'self' bcz code must be suitable for all programmers.
    def change1(ritik):
        print(f"change value is {ritik.a}")



obj=Attributes()
obj.change()
obj.a=4
obj.change1()

