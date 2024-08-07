
#this will print harry software devloper 
class person:
 name = "harry"
 occupation = "software devloper"
 networth = '$10'

#self info of person
 def info(self):
  print(f"{self.name} is a {self.occupation} his networth is{self.networth}")

#list of person
a = person()
b = person()
c = person()

a.name = "akshay"
a.occupation = "actor"
#print(a.name,a.occupation)
a.info()

b.name = "ayush"
b.occupation = "HR"
b.networth ="$2000"
#print(b.name,b.occupation,b.networth)
b.info()

c.name = "alok"
c.occupation = "writter"
c.networth ="$4000"
c.info()
