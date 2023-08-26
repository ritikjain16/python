list=[3,53,20.23,'R',True,"Ritik"]

# for getting the items of list with index

# index=0
# for item in list:
#     print(f"{index}. {item}")
#     index+=1



# shortcut by using enumerate

# but we have to write index first and then item. OR write item at last --REMEMBER
for index,item in enumerate(list):
    print(f"{index}. {item}")