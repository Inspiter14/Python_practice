class Employee:
    CompanyName="TCS" #it's as like static
    def cal():
        print("Good")
    def __init__(self):
        self.sal=0
    def input(self):
        self.__empid=int(input("Enter a  Employee Id"))
        self._ename=input("Enter a Ename")
    def show(self):
        c=22
        print("Employee id",self.__empid)
        print("Employee NAme",self._ename)
        print("Employee Salary",self.sal)
        print("Company Name",Employee.CompanyName)
    

e=Employee()
e.input()
x=Employee()
x.input()
Employee.CompanyName="Infosys"
Employee.cal()
print(e._ename)
#print(e.__empid)

e.show()
