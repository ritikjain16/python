import random
# generates a random no. by importing random

def game(comp,you):
    if comp==you:
        return None

    if comp=="r" and you == "s":
        return False

    elif comp=="r" and you == "p":
        return True

    elif comp=="s" and you == "p":
        return False

    elif comp=="s" and you == "r":
        return True

    elif comp=="p" and you == "r":
        return False
        
    elif comp=="p" and you=="s":
         return True
        
    

randNo = random.randint(1, 3)
if randNo == 1:
    comp="r"
elif randNo==2:
    comp="p"
elif randNo==3:
   comp="s"

print("\nComputer has choosed its choice. Now Your turn :")
you = input("Enter your choice from Scissor(s), Paper(p) and Rock(r) : ")
print("you choose",you,"and computer choose",comp)

g=game(comp,you)

if(g==None):
    print("Match has been tied!")
elif g==True:
    print("You won the match!")
elif g== False:
    print("You Lose the match!")

