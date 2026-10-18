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
if(computer == you):
    print("Its a draw")

else:

    '''
        if(computer ==- 1 and you == 1):#(computer - you) =- 2
                print("You win!")

        elif(computer ==- 1 and you == 0):# (computer - you) =-1
            print("You Lose!")

        elif(computer == 1 and you ==- 1): #(computer - you) =2
            print("You lose!")

        elif(computer == 1 and you == 0):# (computer - you)= 1
            print("You Win!")

        elif(computer == 0 and you ==- 1):# (computer - you) =1
            print("You Win!")

        elif(computer == 0 and you == 1): #computer - you)=-1
            print("You Lose!")

        The below logic is written on the basis of the value of computer - you
    '''

    if((computer- you) ==- 1 or (computer - you) == 2 ):
            print("You lose")
    else:
            print("yòu win")