# we will use 'with'  - it automatically closes the file.

# with open('04.txt','r') as f:
#     data=f.read()

with open('04.txt','w') as f:
    data=f.write("Pragati")

print(data)