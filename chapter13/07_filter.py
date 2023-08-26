def greater(n):
    if n>5:
        return True
    else:
        return False

l=[1,2,3,4,5,98,48,546,20,25,63,24]

# syntax -- > filter(func,list)

print(list(filter(greater,l)))


# for lambda
d=lambda n: n>20
print(list(filter(d,l)))



# also use for tuple
t=(1,35,68,95,45,0)
print(tuple(filter(greater,t)))