class Employee:
    company="ITC"
    name="Default name"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")

class Coder:
    language="python"
    def printLanguages(self):
        print(f"Out of all the languages here is your language:{self.language}")

class programmer(Employee, Coder):
    company="ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.showLanguage} language")


a=Employee()
b=programmer()

b.show()
b.printLanguages()
b.showLanguage()