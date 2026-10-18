a=int(input("Enter your ages:"))
# if elif else ladder
if(a>=18):
    print("you are avobe the age of consent")
    print("Good for you")
elif(a<0):
    print("You are entering an invalid negative age")

elif(a == 0):
    print("You are entering 0 which is not a valid age")
else:
    print("you are bellow  the age of consent")

print("End of program")