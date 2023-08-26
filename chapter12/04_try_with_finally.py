try:
    a=int(input("Enter a no. : "))
    c=1/a

except Exception as e:
    print(e)
    exit()


# finally always executes even also when we exit the above code. 
finally:
    print("We were successful.")


print("Thanks for using this code.") # executes only when program does not give error but 'finally' executes always.