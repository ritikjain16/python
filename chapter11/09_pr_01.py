class C2vec:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j
    
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"


class C3vec(C2vec):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap=k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"


v2=C2vec(2,3)
v3=C3vec(3,4,5)
print(v2)
print(v3)