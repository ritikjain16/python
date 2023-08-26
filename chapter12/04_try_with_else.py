try:
    a=int(input("Enter a no. : "))
    c=1/a

except Exception as e:
    print(e)

# else only executes when try code is true.
else:
    print("We were successful.")