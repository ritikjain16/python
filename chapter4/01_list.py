# Creating a list using []
a=[1,24,56,45]
print(a)

#we can create a list of different data types.
b=[1,"Ritik",True,6.23]
print(b)

#Similar to string ,list also starts with index[0]
print(a[0])
print(b[1])


#But in string we cannot change the string, but we can do change in lists. LISTS ARE MUTABLE.
a[0]=12
print(a)

b[2]="Jain"
print(b)

#Also we can do list slicing (like string slicing)
print(a[0:2])
print(b[1:3]) # [first_index- include,second index-exclude]

print(a[0:])
print(b[:4])


print(a[-4:-1])
print(a[-4:])

#skipping
print(a[0:4:2])
print(b[0:4:2])


