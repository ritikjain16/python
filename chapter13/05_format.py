name="Ritik"
type="boy"
# a=f"This is {name}"   # use fstring

# but in old versions of python we use format

# a="This is {}".format(name)
# a="{} is a good {}".format(name,type)
a="{0} is a good {1}".format(name,type)    # give index according to your choice, starts from 0.
b="{1} is a good {0}".format(name,type)    # give index according to your choice, starts from 0.




print(a)
print(b)