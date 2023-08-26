class Vector:
    def __init__(self,vec):
        self.vec=vec
    
    def __len__(self):
        return len(self.vec)

v1=Vector([1,2,3,4])
v2=Vector([1,5,8])

print(len(v1))
print(len(v2))