class DemoClass:
    a = 10

    def __init__(self) :
        print('Welcome to Automatic Introduction')

    def showvalue(self):
        print('The value is: ', self.a)
        self.c = self.a * self.a
        print(self.c)

    def showvalue2(self):
        print('Welcome to learning')
    
    def showvalue3(self, a, b):
        print(a + b)

obj = DemoClass()
obj.showvalue()
obj.showvalue2()
obj.showvalue3(10, 30)