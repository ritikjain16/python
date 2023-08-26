# l=["Ritik",1,True,'R',"Pragati",25.36,None]   # not work
l=["Ritik","Pragati","Jain's"]  # only use for string

#  we can add a particular word or string after every item in list or tuple by    --    "word".join(listName)

sentence=" and ".join(l)
print(sentence)

sentence="\n".join(l)
print(sentence)

print(type(sentence))