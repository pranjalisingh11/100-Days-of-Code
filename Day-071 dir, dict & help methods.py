# DIR()
x = [1, 2, 3]
print(dir(x))

#DICT()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1

p = Person("John", 30)
print(p.__dict__)

#HELP()
print(help(Person))