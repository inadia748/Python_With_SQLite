class A:
    def displayA(self):
        print('Welcome to A')

#inheritance
class B(A):
    def displayB(self):
        print('Welcome to B ')


# multilevel inheritance

class C(B):
    def displayC(self):
        print('Welcome to C')


# multiple inheritance
'''
class C(A, B):
    def displayD(self):
        print('Welcome to D')
        
'''




'''
obj = B()
obj.displayA()
obj.displayB()

'''

obj = C()
obj.displayC()
obj.displayB()
obj.displayA()


