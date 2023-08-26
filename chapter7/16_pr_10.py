n=int(input("Enter the no. "))

l=[10,9,8,7,6,5,4,3,2,1]

for i in l :
    print(n,"X",i,"=",n*(i))

l2=[]
for i in range(1,11):
    l2.append(f"{n} X {i} = {n*i}")

l2.reverse()
print(l2)
 