class Person:
    def __init__(self, n,o,p):
        self.name = n
        self.occ = o
        self.phone = p


    def info(self):
        print(f"{self.name} is a {self.occ} their phone {self.phone}")

a = Person("akshay","web dev","MI")
b = Person("diviya", "worker","oppo")
c = Person("alok","writer","iphone")
a.info()
b.info()
c.info()
