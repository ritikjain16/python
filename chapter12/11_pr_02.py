l=[1,2,3,4,5,6,7,8,9,10]

for index,item in enumerate(l):
    if index==2 or index==4 or index==6:   # index starts form 0. so 3rd element is at index 2 and so on.
        print(item)   