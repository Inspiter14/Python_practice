class A:
    def __init__(self):
        self.x=10
    def show(self):
        print("X of A Class",self.x)

class C:
    def __init__(self):
        self.z=50
    def show2(self):
        print("Z of C Class",self.z)

class B(A,C):
    def __init__(self):
        A.__init__(self)
        C.__init__(self)

        self.y=10
    def show1(self):
        print("X in B Class",self.x)

        print("Y of B Class",self.y)


b1=B()
b1.show()
b1.show2()
b1.show1()

