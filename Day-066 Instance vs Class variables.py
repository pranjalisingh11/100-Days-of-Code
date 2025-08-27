#INSTANCE VARIABLE
class Employee:
    companyName = "Apple"  #class variable -> applicable in all the instances
    noOfEmployee = 0
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
        Employee.noOfEmployee += 1

    def showDetails(self):
        print(f"The name of Employee is {self.name} and  the raise amount in {self.noOfEmployee} sized {self.companyName} is {self.raise_amount}")

#these are associated with instance variable
emp1 = Employee("Harry")
emp1.raise_amount = 0.3
emp1.companyName = "Apple india" # it will give Apple India because first ye dekha jata hai ki instance variable present hai to ye isko show krega and if ni milega tab class variable ko show krta hai
emp1.showDetails()
emp2 = Employee("Gungun")
emp2.raise_amount = 0.4
emp2.showDetails()

