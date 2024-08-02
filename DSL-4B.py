class Assign4b:
    def getInput(self):
        rollno= []
        n = int(input("Enter total students who attended training program : "))
        for i in range(n):
            student = int(input("Enter students rollno : "))
            rollno.append(student)
        print("Students who attended training are : ",rollno)
        return rollno , n

    def sort(self,rollno ,n):
        temp =0
        i=0
        j=0
        for i in range(n-1):
            for j in range(n-i-1):
                if(rollno[j]>rollno[j+1]):
                    temp = rollno[j]
                    rollno[j] = rollno[j+1]
                    rollno[j+1] = temp

    def binarysearch(self,rollno ,n,rollsearch): #binary iterative
        low = 0
        high = n-1
        while(low<=high):
            mid = int((low+high)/2)
            if(rollno[mid] < rollsearch):
                low = mid+1
            elif(rollno[mid] > rollsearch):
                high = mid-1
            else:
                return print("Roll No ",rollsearch," attended the program")
        return print("This Roll no not attended training program.")

    def recursive_search(self,rollno,low,high,rollsearch): #binary recursive
        #object.sort(rollno,n)
        if(low == high):
            if(rollno[low] == rollsearch):
                return print("Roll No ",rollsearch," attended the program")
        else:
            mid = int((low+high)/2)
            if(rollno[mid] == rollsearch):
                return print("Roll No ",rollsearch," attended the program")
            elif(rollno[mid]<rollsearch):
                return object.recursive_search(rollno,mid+1,high,rollsearch)
            else:
                return object.recursive_search(rollno,low,mid-1,rollsearch)
        return print("This Roll no not attended training program.")

    def fibonacci_Search(self,rollno,rollsearch,n):
        object.sort(rollno,n)
        f=0
        a,b=0,1
        c=a+b
        while c<n:
            a=b
            b=c
            c=a+b
        offset=-1
        
        while c>1:
            i=min(offset+a,n-1)
            if rollno[i]<rollsearch:
                c=b
                b=a
                a=c-b
                offset=i
            elif rollno[i]>rollsearch:
                c=a
                b=b-a
                a=c-b
            else:
                print("Roll No ",rollsearch," attended the program")
                f=1
                break
        if f==0 and b!=0 and rollno[offset+1]==rollsearch:
            print("Roll No ",rollsearch," attended the program")
            exit
        if f==0:
                  print("Roll No: ",rollsearch," didn't attend the program")
                  
        


    def choice(self):
        while True:
            print("1.Binary search.")
            print("2.Recursive Binary search.")
            print("3.Fibonacci Search.")
            choice1 = int(input("Enter your choice : "))
            if choice1==1:
                object.sort(rollno, n)
                print("Sorted list of rollno : ", rollno)
                rollsearch = int(input("Enter rollno to search in list : "))
                object.binarysearch(rollno, n,rollsearch)
            if choice1==2:
                low = 0
                high = n - 1
                object.sort(rollno,n)
                print("Sorted list of rollno : ", rollno)
                rollsearch = int(input("Enter rollno to search in the list :"))
                object.recursive_search(rollno,low,high,rollsearch)
            if choice1==3:
                object.sort(rollno,n)
                print("Sorted list of rollno : ", rollno)
                rollsearch = int(input("Enter rollno to search in the list :"))
                object.fibonacci_Search(rollno,rollsearch,n)
                
            userinput = input("do you want to continue?y/n")
            if userinput in 'Yy':
                continue
            else:
                break
object = Assign4b()
rollno ,n = object.getInput()
object.choice()
