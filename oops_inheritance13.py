# inheritance = allow a class to inherit attributes and methods from another class
#               help with code reusebility and extensibility
#               class child(parent):

class employee:               # PARENT CLASS
    employeecount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        employee.employeecount=employee.employeecount+1
class part_time(employee):        # CHILD CLASS of employee
    def display_info(self):
        return f"name = {self.name} and salary is $ {self.salary:.2f} working as a part time"
class full_tiime(employee):       # CHILD CLASS of employee
    def display_info(self):
        return f"name = {self.name} and salary is $ {self.salary:.2f} working as a full time"

employee1=part_time("Mahidhar",99999)      # OBJECT 1
employee2=full_tiime("Srimanth",9999999)   # OBJECT 2


print(employee1.display_info())
print(employee2.display_info())

print(employee.employeecount)


