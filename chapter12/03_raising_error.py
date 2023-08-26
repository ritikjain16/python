def increment(num):
    try:
        return int(num) + 1
    
    # we can make our own statements on an error by raising the error.
    except:
        raise ValueError("Value Error")

a=increment(4)
# a=increment('klbv')

print(a)

