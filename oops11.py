# OBJECT = A "bundle" of related attributes (variables) and methods (function)
#          Ex. phone,cup,book
#          you need a "class" to create many object
#
# CLASS = (blueprint) used to design the structure and layout of an object
# ..............................................................................

class student:              # classs

    def __init__(self,name,year,branch,id): # constrictor
        self.name=name            # attributes
        self.year=year            # attributes
        self.branch=branch        # attributes
        self.id=id                # attributes
    def is_passedout(self):       # methods
        if self.year+4<=2025:
            return True
        else:
            return False
    def detals(self):             # methods
        print(f"{self.name} is belongs to {self.branch} and pass out is {self.year+4} ")


student1=student("mahidhar",2021,"CSE",20560)   # object

print(student1.name)
print(student1.is_passedout())
student1.detals()


