# n = (n*(n+1))/2
# n = 1 + 2 + 3 ..... (n-1) + n
# sum(n) = sum(n-1) + n


def sum(n):
    # print(int((n*(n+1)/2)))   # Iterative

    # OR
    if n == 1:     # Recursive
        return 1
    else:
        return sum(n-1)+n


print(sum(20))
