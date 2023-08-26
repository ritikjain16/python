num=int(input("Enter the no. : "))

table=[num*i for i in range(1,11)]
print(f"Check your table of {num} in tables.txt file.")

with open("tables.txt","a") as f:    # using append mode.
    f.write(str(table))
    f.write("\n")