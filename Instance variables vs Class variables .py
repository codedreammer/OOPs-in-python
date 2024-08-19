class Employee:
    companyName = "Apple"
    def __init__(self,name):
        self.name = name 
        self.raise_amount = 0.02
        self.location = "america"
    def showDetailes(self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.companyName} is {self.raise_amount} location is {self.location}")

emp1 = Employee("harry")
emp1.raise_amount = 0.3
emp1.companyName = "Apple India"
emp1.showDetailes()
print(Employee.companyName)

emp2 = Employee("akshay")
emp2.raise_amount = 0.44
emp2.companyName = "Amazon"
emp2.showDetailes()
print(Employee.companyName)

