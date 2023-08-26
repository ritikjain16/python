# syntax -- reduce(func,list)

from functools import reduce


l=[1,2,3,4,5]

sum=lambda a,b: a+b
print(reduce(sum,l))

