n=int(input("Enter the no. "))

prime=True
for i in range(2,n):
    if(n%i==0):
        prime=False
        break

if prime:
    print("Prime no.")
else:
    print("Not a Prime no.")            