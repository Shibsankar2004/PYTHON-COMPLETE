a=int(input("Enter your ages:"))
# if elif else ladder
# if statement 1
if(a%2==0):
    print("a is even")
 # end of if statement 1

# if statement 2
if(a>=18):
    print("you are avobe the age of consent")
    print("Good for you")
elif(a<0):
    print("You are entering an invalid negative age")

elif(a == 0):
    print("You are entering 0 which is not a valid age")
else:
    print("you are bellow  the age of consent")
#end of if statement 2 

print("End of program")