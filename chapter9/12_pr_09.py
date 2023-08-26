with open("12f1.txt",'r') as f:
    a=f.read()

with open("12f2.txt",'r') as f:
    b=f.read()

if a==b:
    print("Identical")
else:
    print("Not Identical")

