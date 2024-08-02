class MatrixOper:
    def getMatrix(self):
        r=int(input("Enter the no. of rows:"))
        c=int(input("Enter the no. of columns:"))

        matrix=[]
        print("Enter values row-wise:")
        for i in range(r):
            a=[]
            for j in range(c):
                a.append(int(input()))
            matrix.append(a)

        print("The Matrix Formed is:")
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

        print("\nRows in Matrix 1:",row_1)
        print("Columns in Matrix 1:",col_1,"\n")
        print("Rows in Matrix 2:", row_2)
        print("Columns in Matrix 2:", col_2)

        if row_1==row_2 and col_1==col_2:
            for i in range(row_1):
                for j in range(row_1):
                    m1[i][j]=m1[i][j]+m2[i][j]
            print("\nAfter Addition the Matrix Formed is:")
            for i in m1:
                print(i)
        else:
            print("Matrix Addition is not Possible. ")

    def mulMatrix(self):
        m1=self.getMatrix()
        m2=self.getMatrix()

        row_1=row_2=col_1=col_2=0
        result=[]

        for i in m1:
            row_1=row_1+1

        for i in m1[0]:
            col_1=col_1+1

        for i in m2:
            row_2=row_2+1

        for i in m2[0]:
            col_2=col_2+1

        if row_2==col_1:
            for i in range(row_1):
                temp=[]
                for j in range(col_2):
                    a=0
                    for k in range(row_2):
                        a=a+(m1[i][k]*m2[k][j])
                    temp.append(a)
                result.append(temp)

            print("\nMatrix Formed after Multiplication: ")
            for i in result:
                print(i)
        else:
            print("Multiplication not possible. ")

    def transposeMatrix(self):
        m1=self.getMatrix()
        row_1=col_1=0
        result=[]

        for i in m1:
            row_1=row_1+1
        for i in m1[0]:
            col_1=col_1+1

        for i in range(col_1):
            temp=[]
            for j in range(row_1):
                temp.append(m1[j][i])
            result.append(temp)

        print("\nAfter Transpose:")
        for i in result:
            print(i)


m=MatrixOper()
m.addMatrix()
#m.mulMatrix()\
#m.transposeMatrix()
