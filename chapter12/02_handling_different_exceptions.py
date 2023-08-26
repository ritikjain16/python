try:
    a=int(input("Enter a no. : "))
    c=1/a
    print(c)

# other errors

except ValueError as e:
    print("Plz enter a valid Value.")

except ZeroDivisionError as e:
    print("Make sure you are not dividing by 0")

print("Thanks for using this code.")