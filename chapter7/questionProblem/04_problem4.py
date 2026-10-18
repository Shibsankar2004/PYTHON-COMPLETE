n=int(input("Enter a nuymber:"))

for i in range(2,n):
   if(n%i==0):
        print("number is not prime")
        break
if (n <= 1):
    print("Enter a valid number greater than 1")

else:
    print("number is prime")