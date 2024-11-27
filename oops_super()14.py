# super() = function used in a child class to call methods from a parent class (superclass)
#           allows you to extend the functionality of the inherited methods
class human:
    def __init__(self,name,age,colour):
        self.name=name
        self.age=age
        self.colour=colour
    def info(self):
        print(f"{self.name} is a human and age is {self.age} years")
class girls(human):
    def __init__(self,name,age,colour,is_male):
        super().__init__(name,age,colour)  #   calling arguments
        self.is_male=is_male
    def info(self):
        super().info()  #              calling method
        print(f"{self.name} is a Girl.and age is {self.colour} years")
class boys(human):
    def __init__(self,name,age,colour,is_male):
        super().__init__(name, age, colour) #   calling arguments
        self.is_male=is_male
    def info(self):
        super().info() #              calling method
        print(f"{self.name} is a Boy.and age is {self.colour} years")

human1=boys("Mahidhar",21,"skin_colour",True)
human2=girls("elene",15,"white",False)

human1.info()
human2.info()