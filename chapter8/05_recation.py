'''
factorial(1) = 1
factorial(2) = 2 X 1
factorial(3) = 3 x 2x 1
factorial(4) = 4 X 3 X 2 X 1
factorial(5) = 5 x 4 X 3 X 2 X 1



factorial(n) = n * factorial(n-1)

factorial(n) = n X n-1 x ...3x2x1
'''

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)
n=int(input("Enter a number: "))
print(f"The factorial of this number:{factorial(n)}")