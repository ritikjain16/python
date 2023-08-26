def greet(name):
    print(f"Good Morning , {name}")



# if we import this module in another program then full code get executes.
# but if we don't want to execute full code and only wants to execute only method.
# we use  if __name__ == "__main__"

print(__name__)  #-- here it gives main


if __name__ == "__main__":
    n=input("Enter name : ")
    greet(n)