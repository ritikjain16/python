
# 06_pratice_set_04.py

lang={}

a=input("Enter your language Ritik : ")
b=input("Enter your language Pragati : ")
c=input("Enter your language Sanjeev : ")
d=input("Enter your language Ekta : ")

lang['Ritik']=a
lang['Pragati']=b
lang['Sanjeev']=c
lang['Ekta']=d

print(lang)

# if 2 keys are same then its value is latest assigned value
lang['Ritik']=a
lang['Ritik']=b
lang['Sanjeev']=c
lang['Ekta']=d
print(lang) 

# if 2 values are same 
lang['Ritik']=a
lang['Pragati']=a
lang['Sanjeev']=c
lang['Ekta']=d
print(lang) 




