import random
def  game():
    print("You are playing the game...")
    score=random.randint(1,62)
    with open ("hiscore.txt") as f:
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    print(f"your score: {score}")
    if(score>hiscore):
        with open("hiscore.txt","w") as f:
            f.write(str(score))
    return score
game()

'''
Example Run
Case 1: First time playing (file empty)
hiscore.txt contains: "" (empty).

Random score generated: say 25.

Since file is empty → hiscore = 0.

Compare: 25 > 0 → True.

File updated: hiscore.txt now contains "25".

Output:

Code
You are playing the game...
your score: 25
New high score saved!




Case 2: Next time playing (file has 25)
hiscore.txt contains: "25".

Random score generated: say 18.

File read → hiscore = 25.

Compare: 18 > 25 → False.

File not updated (still "25").

Output:

Code
You are playing the game...
your score: 18




Case 3: Another run (file has 25)
hiscore.txt contains: "25".

Random score generated: say 40.

File read → hiscore = 25.

Compare: 40 > 25 → True.

File updated: hiscore.txt now contains "40".

Output:

Code
You are playing the game...
your score: 40
New high score saved!

'''