class Employee:
    language ="java"
    salary=677679

    def __init__(self,name,salary,language):#dunder method which is automatically called
        self.name=name
        self.salary=salary
        self.language=language
        print("I am creating an object")
    def getInfo(self):
        print(f"The language is {self.language}.the salary is{self.salary}")
    @staticmethod
    def greet():
        print("good morning")
shib=Employee("shib",3556,"javascript")
# shib.language="database"
# shib.greet()
# shib.getInfo()
print(shib.name,shib.salary,shib.language)