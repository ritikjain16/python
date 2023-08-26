# a=None

# if a is None:      # 'is' used for checking 
#     print("yes")
# else:
#     print("No")




a=[1,54,78,65]
b=int(input("Enter the no. "))

if(b in a):   # 'in' is used to check in a list,tuple,dict,set. 
    print("yes", a.index(b));
else:
    print("No")    


