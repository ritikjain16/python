# concatenating of string
a="Good Morning , "
b=input("Enter your Name: ")
print(a + b)

# string_slicing
name="Ritik"
print(name[4]) # for printing the character at a position (start from 0)
print(name[0])

# now slicing
print(name[0:4]) # includes 0 but not 4
print(name[0:5])

print(name[:5]) # is same as name[0:5]
print(name[0:]) # is same as name[0:5]

# Reverse slicing
print(name[-5:-1])
print(name[:-1]) # is same as name[0:4]
print(name[-5:]) # is same as name[0:5]



#string with skip value
name1="Ritik Jain"
print(name1[0:10:2])  # skips every second character
# or
print(name1[::2])