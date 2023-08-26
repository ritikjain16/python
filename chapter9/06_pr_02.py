def game():
    n=int(input("Enter your score : "))
    return n

score = game()
with open('06.txt','r') as f:
    a = f.read()

if int(a)<score:
    with open('06.txt','w') as f:
     f.write(str(score))
     print("You had scored high score! plz check the score file (06.txt).")

elif a=='':
    with open('06.txt','w') as f:
     f.write(str(score))

elif int(a)>score:
     print("Low Score! Try again!")


    