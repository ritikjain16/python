with open("11.txt",'r') as f:
    a = f.read()

with open("11_this.txt",'w') as f:
    f.write(a)