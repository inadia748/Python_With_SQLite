class Student:
    __name = 'Nadia' # private variable

    def __init__(self):
        print(self.__name)
        self.__displayinfo()

    # private function
    def __displayinfo(self):
        print('It is a private function')



obj = Student()

# here, private variable and function cannot be accessed by obj.__name and obj.__displayinfo(). It can only be accessed by a constructor.




