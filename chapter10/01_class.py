class Employee:
    name="Harry"
    language="py" #this  is a class  atribute
    salary=120000



harry=Employee()
harry.name="Harry"#this is an instance attribute
print(harry.language,harry.salary)


rohan=Employee()
rohan.name="Rohan Roro Robinson"#this is an instance attribute
print(rohan.salary,rohan.language) 

# Here name is object attribute and salary and 
# language are class attributes as  they directly belong to the class