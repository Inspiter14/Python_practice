#Tallest between two persons object as parameter and Returning 
class Person:
    def __init__(self):
        self.name=input("Enter a Name")
        self.height=int(input("Enter a Height"))
    def show(self):
        print("Name ",self.name)
        print("Name ",self.height)
    def compare(self,obj):
        if self.height >obj.height:
            self.show()
        else:
            obj.show()
    def __gt__(self,obj):
        if self.height >obj.height:
            return self
        else:
            return obj
    def __gt__(self,obj):
        if self.height >obj.height:
            return True
        else:
            return False

p1=Person()
p2=Person()

if p1>p2:
    p1.show()
else:
    p2.show()
