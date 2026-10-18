# c/5=(f-32)/9

def f_to_c(f):
    return 5*(f-32)/9
f=int (input("Enter temperature in F:"))
print(f"{round(f_to_c(f),2)} °C")