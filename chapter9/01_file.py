
# to open a file

f=open('01.txt','r')   # write mode
# data = f.read()  # reads full file
data = f.read(5)   # reads only first 5 characters
print(data)

f.close()