def divisible5(n):
    if(n%5==0):
        return True
    return False

a=[1,2,3455,6789,2345,56770,55]
f=list(filter(divisible5,a))
print(f)