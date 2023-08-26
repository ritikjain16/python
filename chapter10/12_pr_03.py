class Attributes():
    a=3

obj=Attributes()
# obj.a=4

print(obj.a)
# it do not change the class attribute as it is an instance attribute

# but we can change the class attribute by
Attributes.a=6
print(obj.a)
