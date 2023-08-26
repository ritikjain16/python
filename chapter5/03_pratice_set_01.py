# 03_pratice_set_01.py

dicto = {
 "Rail":"Train",
 "Pankha":"Fan",
 "Papa":"Father"
}

print("\noptions are : " ,dicto.keys())
a=input("Enter the Hindi word\n")

# print("English Translation is :", dicto[a]) # not use bcz throws an error on wrong key

print("English Translation is :", dicto.get(a))