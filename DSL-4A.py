class Assignment_4:
    def getInput(self):
        rollno = []
        # rollsearch = 0
        n = int(input("Number of students : "))
        for i in range(0,n):
            student = int(input("Enter student's rollno : "))
            rollno.append(student)
        print("Roll numbers are : ",rollno)
        # rollsearch = int(input("Enter rollno to search in list : "))
        return rollno,n

    def sequential_search(self,rollno , n):
        rollsearch = int(input("Enter rollno to search in list : "))
        i=0
        for i in range(n):
            if(rollno[i] == rollsearch):
                return print("Rollno has attended the training program")
        return print("This rollno has not attended the training program")

    def sentinal_search(self,rollno ,n):
        rollsearch = int(input("Enter rollno to search in list : "))
        rollno.append(rollsearch)
        i=0
        while(rollno[i]!=rollsearch):
            i=i+1
        if(i<n):
            return print("Rollno has attended the training program")
        return print("This rollno has not attended the training program")

    def choice(self):
        while True:
            print("1.Sequential search.")
            print("2.Sentinal search.")
            choice1 = int(input("Enter your choice : "))
            if choice1==1:
                object.sequential_search(rollno, n)
            if choice1==2:
                object.sentinal_search(rollno, n)
            userinput = input("do you want to continue?y/n")
            if userinput in 'Yy':
                continue
            else:
                break

object = Assignment_4()
rollno , n = object.getInput()
object.choice()
