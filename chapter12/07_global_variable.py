# a=45 # global variable

# def func():
#     a=8  # local variable
#     print(a)

# func()   # by local variable
# print(a) # by global variable






# if we want to change the global variable for all.
a=45 # global variable

def func():
    global a  # by writing this a changes globally
    print(a)
    a=8  # local variable if global keyword is not used
    print(a)

func()   # by local variable
print(a) # by global variable