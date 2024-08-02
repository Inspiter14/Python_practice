class SetOper:
    def getInput(self):
        cricket=[]
        badminton=[]
        football=[]
        print("Enter the names who plays cricket: ")
        for i in range(0,3):
            cricket.append(input())

        print("Enter the names who plays badminton: ")
        for i in range(0, 3):
            badminton.append(input())

        print("Enter the names who plays football: ")
        for i in range(0, 3):
            football.append(input())

        print("Cricket: ",cricket)
        print("Badminton: ",badminton)
        print("FootBall: ",football)

        return cricket,badminton,football

    def bothcriandbad(self,cricket,badminton):
        result=[]
        for i in range(3):
            for j in range(3):
                if cricket[i]==badminton[j]:
                    result.append(cricket[i])
        print("Students who play both Badminton and Cricket are/is: ",result)
        return result

    def eithercriorbad(self,cricket,badminton):
        result=[]
        for i in range(3):
            found=False
            for j in range(3):
                if badminton[i]==cricket[j]:
                    found=True
            if found==False:
                result.append(badminton[i])

        for i in range(3):
            found=False
            for j in range(3):
                if cricket[i]==badminton[j]:
                    found=True
            if found==False:
                result.append(cricket[i])
        print("either Cricket or Badminton but not both:",result)
        return result

    def onlyfoot(self,cricket,badminton,football,r1,r2):
        result=[]
        cnt=0
        for i in range(3):
            flag=0
            for j in range(3):
                if football[i]==r1[j]:
                    flag=1
                break
            for k in range(3):
                if football[i]==r2[k]:
                    flag=1
                break
            if flag==0:
                result.append(football[i])
                cnt=cnt+1

        print("Number of students who play Only Football: ",result,cnt)

    def onlycriandonlyfootnotbad(self,cricket,badminton,football):
        result1=[]
        result2=[]
        cnt=0
        for i in range(3):
            flag=0
            for j in range(3):
                if cricket[i]==badminton[j]:
                    flag=1
            if flag==0:
                result1.append(cricket[i])
        print("Only Cricket:",result1)

        for i in range(3):
            flag1=0
            for j in range(3):
                if football[i]==badminton[j]:
                    flag1=1
            if flag1==0:
                result2.append(football[i])
        print("Only Football:",result2)

s=SetOper()
cri,bad,foot=s.getInput()
r1=s.bothcriandbad(cri,bad)
r2=s.eithercriorbad(cri,bad)
s.onlyfoot(cri,bad,foot,r1,r2)
s.onlycriandonlyfootnotbad(cri,bad,foot)



