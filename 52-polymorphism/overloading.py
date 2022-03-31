class WL:
    def displayinfo(self, name = ''):
        print("Welcome to WLearning " + name)

obj = WL()
obj.displayinfo()
obj.displayinfo('Nadia')


# overloading concept is same function is doing different jobs.
# Here, obj.displayinfo() returns "Welcome to Wlearning"
# while, obj.displayinfo('Nadia') returns "Welcome to WLearning Nadia"