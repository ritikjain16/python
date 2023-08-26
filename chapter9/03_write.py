# f=open('03.txt','w')  # write mode (file automatically generates if it is not already exist.)
# f.write("Ritik")      # in write mode, file overwrites .
# f.close()





f=open('03.txt','a')  # append mode
f.write(" Ritik")      # in append mode text appends at last in file every time.
f.write(" Pragati")
f.close()