class Employee:
    language="java" # This is a class attribute
    salary=5566873
    def getInfo(self):
        print(f"The language is {self.language}.The salary is:{self.salary}")
shib=Employee()
shib.language="javascript"#this is a instance attribute
# print(shib.language,shib.salary)
shib.getInfo()
# Employee.getInfo(shib)