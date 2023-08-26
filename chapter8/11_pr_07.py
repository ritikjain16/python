# s = "     Ritik is a good boy   "
# print(s)
# print(s.strip())


def remove_and_strip(string,word):
    n=string.replace(word,"")
    return n.strip()

s = "     Ritik is a good boy   "
n1 = remove_and_strip(s,"good ")
print(n1)