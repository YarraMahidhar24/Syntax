# "Duck typing' = Another way of achieve polymorphism besides inheritance
#                 Object must have the minimum necessary attributes /methods
#                 "if it look like a duck and quacks like a duck, it must be a duck."

from abc import abstractmethod
class animel:
    @abstractmethod
    def is_leaving(self):
        pass
    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def sleep(self):
        pass
class land(animel):
    def is_leaving(self):
        return(True)
    def eat(self):
        return("Eats food")
    def sleep(self):
        return("it will sleep")
class water(animel):
    def is_leaving(self):
        return(True)
    def eat(self):
        return("Eats food")
    def sleep(self):
        return("it will sleep")
class air(animel):
    def is_leaving(self):
        return(True)
    def eat(self):
        return("Eats food")
    def sleep(self):
        return("it will sleep")
class human:
    def is_leaving(self):
        return(True)
    def eat(self):
        return("Eats food")
    def sleep(self):
        return("it will sleep")

l=[land(),air(),water(),human()]
for l in l:
    #print(classmethod(l))
    print(l.is_leaving())
    print(l.sleep())
    print(l.eat())
    print()
# So hear human is eats and sleep as same as animels then human is also an animel
