#Matrix Operations
class MatrixOper:
    def getMatrix(self):
        r=int(input("Enter the Number of Rows:"))
        c=int(input("Enter the Number of Columns:"))

        matrix=[] #initialize matrix
        print("Enter the Entries according to row")

        #take user input
        for i in range(0,r):
            a=[]
            for j in range(0,c):
                a.append(int(input()))
            matrix.append(a)

        #printiing Matrix
        print("Formed Matrix is:")
        for i in matrix:
            print(i)

        return matrix

    def addMatrix(self):
        m1=self.getMatrix()
        m2=self.getMatrix()

        row_1=row_2=col_1=col_2=0
        for i in m1:
            row_1=row_1+1
        for i in m1[0]:
            col_1=col_1+1
        for i in m2:
            row_2=row_2+1
        for i in m2[0]:
            col_2=col_2+1
        print("For Matrix 1:\nThe no. of Rows are:",row_1,"\nThe no. of Columns are:",col_1)
        print("For Matrix 2:\nThe no. of Rows are:", row_2, "\nThe no. of Columns are:", col_2)

        if(row_1!=row_2 and col_1!=col_2):
            print("The Addition is not possible !")
        else:
            for i in range(row_1):
                for j in range(row_1):
                    m1[i][j]=m1[i][j]+m2[i][j]
            print("Addition is:")
            for i in range(row_1):
                for j in range(col_1):
                    print(m1[i][j], end = " ")
                print()

    def subMatrix(self):
        m1 = self.getMatrix()
        m2 = self.getMatrix()

        row_1 = row_2 = col_1 = col_2 = 0
        for i in m1:
            row_1 = row_1 + 1
        for i in m1[0]:
            col_1 = col_1 + 1
        for i in m2:
            row_2 = row_2 + 1
        for i in m2[0]:
            col_2 = col_2 + 1
        print("For Matrix 1:\nThe no. of Rows are:", row_1, "\nThe no. of Columns are:", col_1)
        print("For Matrix 2:\nThe no. of Rows are:", row_2, "\nThe no. of Columns are:", col_2)

        if row_1 == row_2 and col_1 == col_2:
            for i in range(row_1):
                for j in range(row_1):
                    m1[i][j] = m1[i][j] - m2[i][j]
            print("Subtraction is:")
            for i in range(row_1):
                for j in range(col_1):
                    print(m1[i][j], end=" ")
                print()
        else:
            print("The Subtraction is not possible !")

    def mulMatrix(self):
        m1=self.getMatrix()
        m2=self.getMatrix()

        row_1 = row_2 = col_1 = col_2 = 0
        result=[]

        for i in m1:
            row_1 = row_1 + 1
        for i in m1[0]:
            col_1 = col_1 + 1
        for i in m2:
            row_2 = row_2 + 1
        for i in m2[0]:
            col_2 = col_2 + 1
        print("For Matrix 1:\nThe no. of Rows are:", row_1, "\nThe no. of Columns are:", col_1)
        print("For Matrix 2:\nThe no. of Rows are:", row_2, "\nThe no. of Columns are:", col_2)

        if row_2==col_1:
            for i in range(row_1):
                temp=[]
                for j in range(col_2):
                    a=0
                    for k in range(row_2):
                        a=a+(m1[i][k]*m2[k][j])
                    temp.append(a)
                result.append(temp)

            for i in result:
                print(i)
        else:
            print("Matrix Multiplication is not possible !")

    def transposeMatrix(self):
        m1=self.getMatrix()
        result=[]

        row_1=col_1=0
        for i in m1:
            row_1=row_1+1
        for i in m1[0]:
            col_1=col_1+1

        for i in range(col_1):
            temp=[]
            for j in range(row_1):
                temp.append(m1[j][i])
            result.append(temp)

        print("Transpose of Matrix is:")
        for i in result:
            print(i)



m=MatrixOper()
m.addMatrix()
#m.subMatrix()
#m.mulMatrix()
#m.transposeMatrix()

