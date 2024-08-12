class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"the name of Employee: {self.id} is {self.name}")

class programmer(Employee):
    def showLanguage(self):
        print("the defaultlanguage is python")

class system(Employee):
    def showsystemname(self):
        print("he use Linex")

e1 = system("alok", 400)
e1.showDetails()
e1.showsystemname()
e2 = programmer("akshay", 4000)
e2.showDetails()
e2.showLanguage()

        