# try except are used when we don't want an error.

while(True):
    print("press q to quit")
    a=input("Enter a no. : ")
    if a=='q':
     break
    try:
     a=int(a)
     if a>6:
        print("Greater than 6")

    except Exception as e:    # by except we know the exception without getting an error
      print(e)




print("Thanks for Using this code!")