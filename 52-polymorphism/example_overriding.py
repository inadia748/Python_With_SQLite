class A:
    def showData(self):
        print(' I am in A class')

class B(A):
    def showData(self):
        print(' I am in B class')


obj = B()
obj.showData()