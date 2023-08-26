f1=int(input("Enter marks of  1  subject : "))
f2=int(input("Enter marks of  2  subject : "))
f3=int(input("Enter marks of  3  subject : "))
f4=int(input("Enter marks of  4  subject : "))

marks=[f1,f2,f3,f4]
print("Your total marks is : ")
print(marks[0] + marks[1] + marks[2] + marks[3]) 

# or by using sum property of python language
print(sum(marks))