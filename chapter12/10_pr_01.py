def file1(filename):
    try:
        with open(filename,"r") as f:
            print(f.read())
    
    # except:                   # we can use only except:
    except FileNotFoundError:     
        print(f"{filename} not found")

file1("1.txt")
file1("2.txt")
file1("3.txt")

# Now delete a file
