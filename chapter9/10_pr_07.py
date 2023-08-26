a=True
i=1

with open('10.txt','r') as f:
    while a:
      
      a=f.readline().lower() # converts all in lowecase
      if 'python' in a:
        print(f"Python is present on line {i}")
    i+=1
