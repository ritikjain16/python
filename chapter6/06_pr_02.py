m1 = int(input("Enter subject 1 marks : "))
m2 = int(input("Enter subject 2 marks : "))
m3 = int(input("Enter subject 3 marks : "))

if(m1<33 or m2<33 or m3<33):
    print("You are fail bcz you have less than 33% marks in one or more subjects")
elif((m1+m2+m3)/3) < 40:
    print("You are fail bcz your marks are below 40%")
else:
    print("Congratulations! You are pass and your % is",float((m1+m2+m3)/3))    

