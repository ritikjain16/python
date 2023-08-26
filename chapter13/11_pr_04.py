l = [1, 2, 4, 89, 80, 75, 55, 5, 6, 20, 90]

print(list(filter(lambda a: a%5==0,l)))


l2 = []
for i in range(1,251):
    if i%5==0 and i%2==0 and i%3==0:
        l2.append(i)

print(l2)
print(len(l2))