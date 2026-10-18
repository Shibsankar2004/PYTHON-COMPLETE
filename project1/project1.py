# SNAKE , WATERE ,GUN GAME


import random
'''
1 -->snake
-1 -->water
0 -->gan
'''

'''
Winning conditions:

Snake drinks water → snake wins (computer == -1 and you == 1).

Gun kills snake → gun wins (computer == 1 and you == 0).

Water douses gun → water wins (computer == 0 and you == -1).
'''

computer=random.choice([-1,0,1])
youstr=input("Enter your choice: ")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"snake",-1:"water",0:"gan"}
you=youDict[youstr]
print(f"your chose  { reverseDict[you]}\n computer chose { reverseDict[computer]}")

if(computer==you):
    print("Its a draw")
else:
    if(computer==-1 and you==1):
        print("you win!")
    elif(computer==-1 and you==0):
        print("You lose!")
    elif(computer==1 and you==-1):
        print("you lose!")
    elif(computer==1 and you==0):
        print("you win!")
    elif(computer==0 and you==1):
        print("you lose!")
    
    elif(computer==0 and you==-1):
        print("you win!")
    else:
        print("something went wrong!")


'''
import random

1 --> snake
-1 --> water
0 --> gun


youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice (s for snake, w for water, g for gun): ")

if youstr not in youDict:
    print("Invalid choice!")
else:
    you = youDict[youstr]
    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

    if computer == you:
        print("It's a draw!")
    elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
        print("You win!")
    else:
        print("You lose!")

'''