for i in range(1,9):
    print(i)
    if(i==4):
        break

# here else not executes bcz break ends the loop
else:
    print("else of for")

for i in range(1,9,2):
     if(i==4):
        continue
     print(i)

# here else  executes bcz continue only skips the value not ends the loop
else:
    print("else of for")

