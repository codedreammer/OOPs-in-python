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

class laptop(Employee):
    def showlaptop(self):
        print("he use asus laptop")

e1 = system("alok", 400)
e1.showDetails()
e1.showsystemname()
e2 = programmer("akshay", 4000)
e2.showDetails()
e2.showLanguage()
e3 = laptop("kumar",300)
e3.showDetails()
e3.showlaptop()


        