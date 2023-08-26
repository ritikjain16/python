class Number():

    def __init__(self,num):
        self.num=num

    def __add__(self,num2):
        print("Let's add")
        return self.num + num2.num
        # return 20

    def __mul__(self,num2):
        print("Let's Multiply")
        return self.num * num2.num

    def __sub__(self,num2):
        print("Let's Subtract")
        return self.num - num2.num

    def __truediv__(self,num2):
        print("Let's Divide")
        return self.num / num2.num

    def __floordiv__(self,num2):
        print("Let's Floor Remainder ")
        return self.num // num2.num


n1=Number(16)
n2=Number(4)    

# whenever we use + operator it calls add function
s= n1 + n2
print(s)

s= n1 - n2
print(s)

s= n1 * n2
print(s)

s= n1 / n2
print(s)

s= n1 // n2
print(s)


