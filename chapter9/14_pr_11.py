import os

oldname="14f1.txt"
newname="14f2.txt"

with open(oldname,"r") as f:
    a=f.read()

with open(newname,"w") as f:
    f.write(a)

#  it only copies but we have to delete the previous file for rename.
# we use import os

os.remove(oldname)

