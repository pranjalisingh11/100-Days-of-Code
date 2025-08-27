# emp.py
class Employee:

    def __init__(self, name):
        self.name = name

    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i

    def __str__(self):
        return f"The name of the employee is {self.name} str"

    def __repr__(self):
        return f"Employee('{self.name}')"

    def __call__(self):
        print("Hey I am good")

#main.py
# from emp import Employee

e = Employee("Harry")
print(str(e))
print(repr(e))
# print(e.name)
# print(len(e))
e()  # call() function



# Quick Quiz Answer -> practical use of __call__ method
class shop:
    def __init__(self,sales,expenditure):
        self.sales=sales
        self.expenditure=expenditure
    def __call__(self):
        print(F"The total profit is {self.sales-self.expenditure}")
shop1=shop(15000,12000)
shop1()