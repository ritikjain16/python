a=[1,6,5,89,45,22,36,69,26,25,100,58,577,5820]


# b=[]
# for item in a:
#     if item%2==0:
#         b.append(item)


# shortcut by list comprehension

b=[i for i in a if i%2==0]
print(b)


c=[i for i in b if i>50]
print(c)


# also set comprehension

t=[1,5,4,3,2,3,2,4]
s={i for i in t}
print(s)