class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name is {self.name}.")

class Dancer:
    def __init__(self,dance):
        self.dance = dance

    def show(self):
        print(f"The dance is {self.dance}.")

class DancerEmployee(Employee, Dancer): #multilevel inheritance - single child class inherits from multiple parent class
    def __init__(self,name,dance):
        self.name = name
        self.dance = dance

o = DancerEmployee("Gungun", "Kathak")
print(o.name)
print(o.dance)
o.show() # it will show() thw first param in the DancerEmployee class
print(DancerEmployee.mro())