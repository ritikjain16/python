with open('08.txt','r') as f:
    a=f.read()

a=a.replace("Donkey","@#$$#@#")

with open('08.txt','w') as f:
        f.write(a)