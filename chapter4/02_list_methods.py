l1=[22,11,66,55,44]


''' WRONG METHOD
lsort=l1.sort() 
print(lsort)      #returns None
'''

#list sorting 
l1.sort()
print(l1)

#list reversing
l1.reverse()
print(l1)


#list append - append value at the end of list
l1.append(16)  # Most important
print(l1)


#list insert
l1.insert(2,33) # insert 33 at index 2
print(l1)


#list pop
l1.pop()  # pop out the last element
l1.pop(2) # pop out the element at index 2
print(l1)

#list remove
l1.remove(22)  # removes the 22 element
print(l1)



