# in python there is no such concepts like access modifiers

#PUBLIC -> by default
class Employee:
    def __init__(self):
        self.name = "Harry"

a = Employee()
print(a.name)

#PRIVATE
class Employee:
    def __init__(self):
        self.__name = "Harry" #private attribute

a = Employee()
# print(a.__name) #cannot be accessed directly
print(a._Employee__name) #can be accessed indirectly -> Name mangling concept
print(a.__dir__())

#PROTECTED
class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()
print(dir(obj))

# calling by object of Student class
print(obj._name)
print(obj._funName())
# calling by object of Subject class
print(obj1._name)
print(obj1._funName())