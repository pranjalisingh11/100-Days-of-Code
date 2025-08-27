# SINGLE INHERITANCE
class ParentClass:
    def parent_method(self):
        print("This is the parent method.")

class ChildClass(ParentClass):
    def child_method(self):
        print("This is the child method.")
        super().parent_method()

child_object = ChildClass()
child_object.child_method()

# MULTIPLE INHERITANCE
class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

class Programmer(Employee): #inheritance
  def __init__(self, name, id, lang):
    super().__init__( name, id) # take this from parent class
    self.lang = lang

rohan = Employee("Rohan Das", "420")
harry = Programmer("Harry", "2345", "Python")
print(harry.name)
print(harry.id)
print(harry.lang)