# class math:
#     def __init__(self, num):
#         self.num = num 

#     def addtonum(self, n):
#         self.num = self.num +n

#     @staticmethod
#     def add(a, b):
#         return a+b
    

# a = math(5)
# print(a.num)
# a.addtonum(6)
# print(a.num)

# print(math.add(7, 2))


# class math :
#     @staticmethod
#     def sub(a,b):
#         return a-b
    
# Result = math.sub(4,3)
# print(Result)

#defference using statice methode and the inheritance property 
class SUM:
    def __init__(self,a,b):
        self.a = 4
        self.b = 3


    def showDetails(self):
        print(f"sum of a,b is {self.a + self.b} ")

e = SUM(4,3)
e.showDetails()
