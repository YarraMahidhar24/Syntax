# static methods = a method that belongs to a class rather than any class (instance)
#                  usually used for general utility function
# Instance methods = Beet for operations on instances of the class (object)
# static methods   = Best for utility function that do not need access to class data
#                    or general utility function #........................[@staticmethod]

# class methods    = Allows operations related to the class itself #......[classmethod]
#                    Take (cls) as the first parameters, which represents the clas itself.
class hostel:
    count=0
    def __init__(self,black,floor,room_no,name,id):
        self.black=black
        self.floor=floor
        self.room_no=room_no
        self.name=name
        self.id=id
        hostel.count+=1
    def getinfo(self): # .......................... Instance method
        return (f"block   = {self.black} "
                f"floor   = {self.floor} "
                f"room_no = {self.room_no} "
                f"name    = {self.name}"
                f"   id      = {self.id}")
    @staticmethod # .................................static method
    def find_room(no):
        if 9>=no>=1:
            return f"the room {no} is in ground floor"
        elif 19>=no>=11:
            return f"the room {no} is in first floor"
        else:
            return "room is not valid"
    @classmethod # .......................class method
    def get_count(cls):
        return f"totel enter are {cls.count}"
hostel1=hostel("C",1,114,"Mahidhar",20560) # object 1
hostel2=hostel("C",1,114,"Elena",20561)    # object 2
print(hostel1.getinfo())
print(hostel2.getinfo())
print(hostel.find_room(11))
print(hostel.get_count())
