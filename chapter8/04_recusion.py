# n! = 1*2*3.......*(n-1)*n
# n != (n-1)! * n


# ITERATIVE PROCEDURE
# n=5
# fac = 1
# for i in range(1,n+1):
#     fac *= i

# print(fac)



# RECURSIVE PROCEDURE
def fac(n):
    if n==0 or n==1:
        return 1
    else:
     return fac(n-1) * n


print(fac(6))

