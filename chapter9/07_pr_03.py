for n in range(2,999):
    with open(f"07_tables/Multiplication_table_of_{n}.txt",'w') as f:
        for i in range(1,11):
            f.write(f"{n} X {i} = {n*i}\n")  
