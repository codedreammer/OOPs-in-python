# class Myclass:
#     def __init__(self, value):
#         self._value = value

    # def show(self):
    #     print(f"Value is {self._value}")

    #  #getters
    # @property
    # def ten_value(self):
    #     return 10* self._value
    
    # #setter
    # @ten_value.setter
    # def ten_value(self, new_value):
    #     self._value = new_value/10
    
# obj = Myclass(10)
# obj.ten_value =67
# print(obj.ten_value)
# obj.show()

class Students:
    def __init__(self,name,rollno,age):
        self.name=name #public
        self._rollno=rollno #protected
        self.__age= age #private
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age>35:
            print("Invalid age give..Age should be less then 35.")

        else:
            self.__age=age

s1=Students("akshay",23,30)
print(s1.get_age())
s1.set_age(34)
print(s1.get_age())
