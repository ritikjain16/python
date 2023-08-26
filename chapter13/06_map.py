def square(num):
    return num*num

l=[1,2,4]

# Method 1
l2=[]
for i in l:
    l2.append(square(i))
print(l2)


# Method 2  -- 
# syntax -- map(func,list)   # func can be a lambda func
print(list(map(square,l)))   # typecast into list


a= lambda n: n+1
print(list(map(a,l)))

# also use for tuple.
t=(1,2,3)
print(tuple(map(a,t)))    # typecast into tuple
