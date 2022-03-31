class WL():
    def displayinfo(self):
        print("Welcome to WLearning")
        

class IIP(WL):
    def displayinfo(self):
        # calling the parent 'WL' function
        super().displayinfo()
        print("Welcome to IIP")
        pass


obj = IIP()
obj.displayinfo()



# Here, you can notice the concept of 'overrriding'
# class IIP and WL have the same function 'def displayinfo()'. 
# So, you notice that class IIP can inherit from class WL. But, the function of 'displayinfo(self)' will return 'Welcome to IIP' instead of returning 'Welcome to WLearning'.

