# polymorphism = greek word that means to "have many forms or faces"
#               poly = many
#               morphe=form
#
#               TWO WAYS TO ACHIEVE POLYMORPHISM
#               1. Inheritance = an object could be treated of same type a parent class
#               2. "duck typing" = object must have necessary attributes/methods
class college:
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id
    def display_info(self):
        print(f"Name  = {self.name}")
        print(f"Age   = {self.age}")
        print(f"ID no = {self.id}")
class students(college):
    def __init__(self, name, age,classroom, id):
        self.classroom=classroom
        super().__init__(name,age,id)
    def display_info(self): #  method overloading
        super().display_info()
        print(f"Room no = {self.classroom}")
class teachers(college):
    def __init__(self, name, age, faculty_room, id):
        self.faculty_room=faculty_room
        super().__init__(name, age, id)
    def display_info(self): #  method overloading
        super().display_info()
        print(f"Room no = {self.faculty_room}")
# obj
student1=students("Mahidhar",21,6011,20560)
student12=students("Elena",21,6011,20561)
teacher1=teachers("Jhansi",21,6012,20562)
teacher2=teachers("Lil",21,6112,69696)
# methods call
# student1.display_info()
# student12.display_info()
# teacher1.display_info()
# teacher2.display_info()
# both are same outputs
k=(student1,student12,teacher1,teacher2)
for i in k:
    i.display_info()
    print()