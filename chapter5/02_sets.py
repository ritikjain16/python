# creating a set by using {} --> set ccontains only non -repititive elements
a={6,4,5,9,7,5} # 5 only prints 1 time.
print(type(a))
print(a)


#this syntax will create an empty dictionary not an empty set
b={}
print(type(b))

#creating an empty set
c=set()
print(type(c))

#adding values to an empty set
c.add(4)
c.add(5)
c.add(6)
c.add(5)  #Repeat value not occurs
# c.add([4,5,6])  # list cannot be add in a set  UNHASHABLE
c.add((4,5,6))  # tuple can be add in a set.
# c.add({"key":"value"}) # dict cannot be add in a set UNHASHABLE 
print(c) 



#length
print(len(c))


#remove
# c.remove(4)  # removes 4 from set c
# c.remove((4,5,6))
# print(c)


#pop
# c.pop()  # pops out the first element
# print(c)
# c.pop()
# print(c)


#clear
# c.clear()
# print(c)



#union
print(c.union({1,2,3,4,5}))

#intersection
print(c.intersection({5,6,9}))
