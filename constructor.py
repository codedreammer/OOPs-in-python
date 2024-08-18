class Person:
    def __init__(self, n,o,p,c):
        self.name = n
        self.occ = o
        self.phone = p
        self.car = c


    def info(self):
        print(f"{self.name} is a {self.occ} their phone {self.phone} and he has {self.car}")

a = Person("akshay","web dev","MI","honda CITY")
b = Person("diviya", "worker","oppo","swif")
c = Person("alok","writer","iphone","lamborgni")
a.info()
b.info()
c.info()
