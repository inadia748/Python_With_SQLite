# getter and setter

class Student:
    def ___init___(self):
        self.___name = ''

    def getname(self):
        return self.__name
    
    def setname(self,name):
        self.__name = name


obj = Student()
obj.setname('Testing')

name = obj.getname()
print(name)

