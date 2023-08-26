with open('09.txt','r') as f:
    a=f.read().lower() # converts all in lowecase

if 'python' in a:
    print("Python is present")
else:
    print("Python is not present")