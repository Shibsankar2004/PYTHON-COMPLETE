def greatestNumber(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c

a=45
b=77
c=45
print(greatestNumber(a,b,c))