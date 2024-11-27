# class variables = shared among all instances of a class
#                   defined out side the constructor
#                   allow you to share data all objects created from that class
# ................................................................................

class employee:
    company_name="Mahidhar_LTD"  # class variables
    company_strength=0           # class variables
    year=2024                    # class variables
    # .............................................
    def __init__(self,name,age):
        self.name=name                 # instant variables
        self.age=age                   # instant variables
        employee.company_strength+=1   # instant variables
        # ................................................

employee1=employee("Mahidhar",21)
employee2=employee("pavan",21)
employee3=employee("rohit",20)

print(employee.company_strength)