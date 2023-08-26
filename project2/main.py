import random

randnumber = random.randint(1, 100)

guess = 0
userNum=None


while userNum!=randnumber:
   userNum = int(input("Enter the Guess no. : "))
   guess += 1
   if userNum == randnumber:
     print("You Guessed it Right!")
   else:
     if userNum < randnumber:
        print("You Guessed it Wrong! Try with Larger No.")
     else:
        print("You Guessed it Wrong! Try with Smaller No.")

print(f"You Guessed it in {guess} guesses.")

    
# storing highcore in a file

with open("highscore.txt",'r') as f:
   hiscore = int(f.read())

if(guess<hiscore):
 print("You have just broken the High Score!")
 with open("highscore.txt",'w') as f:
   f.write(str(guess))

   