marks1=int(input("Sunject one marks:"))
marks2=int(input("Sunject two marks:"))
marks3=int(input("Sunject three marks:"))

total_Parcentage=(100*(marks1+marks2+marks3))/300
if(total_Parcentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed",total_Parcentage)
else:
    print("you are failed try next years",total_Parcentage)