#creating a dictionary by using   "key":"value" pairs.
myDict={
    "Name":"Ritik Jain",
    "Age":"20",
    "Gender":"Male",
    "DOB":"16/8/2000",
    "Marks":[98,95,95,100,84],
    # we can also place another dictionary inside a given dictionary.
    "anotherDict":{
        "Height":"5 feet 8 inch",
        "Color":"Fair",
        5:5.2
    }
}

# Getting the value by its key
print(myDict['Name'])
print(myDict['Marks'])
print(myDict['DOB'])

print(myDict['anotherDict'])
print(myDict['anotherDict']['Color']) # getting the value of color of anotherDict.
print(myDict['anotherDict'][5])


# Dictionaries are MUTABLE 
# myDict['Name']="Pragati"
# print(myDict['Name'])



#get keys by .keys()
print(myDict.keys())
print(type(myDict.keys()))

print(list(myDict.keys())) # can be convert into list.

#get values by .values()
print(myDict.values())


#get items in (key,value) by .items()
print(myDict.items())

#get dictionary
print(myDict)


#we can also update (add) a new key,value pair.
updateDict={
    "Looks":"Smart,Charming",
    "Age":22     # we can also update a key if it is already present in dictionary
}
myDict.update(updateDict)
print(myDict)



#get method
print(myDict.get("Name")) 
print(myDict['Name'])

# #difference between get method and [' ']
print(myDict.get("Name1")) # if we type wrong key then it return NONE.
# print(myDict['Name1'])   # # if we type wrong key then it throws an error. so we may prefer 'get' method.





