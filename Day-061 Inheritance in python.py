class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Emplpoyee: {self.id} is {self.name}")

class Programmer(Employee): # inheritance used
    def showLanguage(self):
        print("The default language is Python")


e1 = Employee("Gungun", 400)
e1.showDetails()
e2 = Programmer("Pranjali", 401)
e2.showDetails()
e2.showLanguage()