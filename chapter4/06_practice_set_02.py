f1=int(input("Enter marks of  1  subject : "))
f2=int(input("Enter marks of  2  subject : "))
f3=int(input("Enter marks of  3  subject : "))
f4=int(input("Enter marks of  4  subject : "))
f5=int(input("Enter marks of  5  subject : "))
f6=int(input("Enter marks of  6  subject : "))
f7=int(input("Enter marks of  7  subject : "))

marksList=[f1,f2,f3,f4,f5,f6,f7]

print("your marks in sorted order is : ")
marksList.sort()
print(marksList)