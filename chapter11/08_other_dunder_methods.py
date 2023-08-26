class Number():

    def __init__(self,num):
        self.num=num

    def __str__(self):
        return f"Decimal Number : {self.num}"
    

n=Number(5)
print(n)