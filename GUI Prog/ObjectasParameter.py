#Tallest between two persons object as parameter and Returning 
class Person:
    def __init__(self):
        self.name=input("Enter a Name")
        self.height=input("Enter a Height")
    def show(self):
        print("Name ",self.name)
        print("Name ",self.height)
    def compare(self,obj):
        if self.height >obj.height:
            self.show()
        else:
            obj.show()
    def compare(self,obj):
        if self.height >obj.height:
            return self
        else:
            return obj

p1=Person()
p2=Person()

p=p1.compare(p2)
p.show()
