class Employee:
    CompanyName="TCS" #it's as like static
    def cal():
        print("Good")
    def __init__(self,id,sal,en):
        self.sal=sal
        self.__empid=id
        self._ename=en
    '''
    def __init__(self):
        self.sal=0
        self.__empid=0
        self._ename="xxx"
    '''
    def __del__(self):
        del self
    def input(self):
        self.__empid=int(input("Enter a  Employee Id"))
        self._ename=input("Enter a Ename")
    def show(self):
        c=22
        print("Employee id",self.__empid)
        print("Employee NAme",self._ename)
        print("Employee Salary",self.sal)
        print("Company Name",Employee.CompanyName)
    
#List of Object as like array of objects
emplist=[]
for x in range(5):
    id=int(input("Enter a id"))
    name=input("Enter a name")
    sal=input("Enter a sal")
    
    e=Employee(id,sal,name)
    emplist.append(e)

for x in emplist:
    x.show()

