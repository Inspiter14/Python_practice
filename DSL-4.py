class AllSortSearch:
    def getInput(self):
        arr=[]
        n=int(input("Enter how many elements you want to insert:"))
        for i in range(n):
            ele=float(input("Enter the roll numbers:"))
            arr.append(ele)
        no=int(input("Enter the roll no to be searched:"))
        return arr,n,no

    def LinearSearch(self,arr,n,no):
        for i in range(n):
            if arr[i]==no:
                print("Roll Number is Present !")
            else:
                print("Roll Number is not Present !")

    def SentinelSearch(self,arr,n,no):
        arr[n]=no
        i=0
        while i!=no:
            i=i+1
        if i<n:
            print("Roll Number is Present !")
        else:
            print("Roll Number is not Present !")


    def Bubble_Sort(self,arr,n):
        for i in range(n):
            for j in range(n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr

    def Binary_Search1(self,arr,n,no): #Iterative
        arr1=self.Bubble_Sort(arr,n)
        low=0
        high=n-1
        mid=0
        while low<=high:
            mid=(low+high)//2
            if no<arr1[mid]:
                low=mid+1
            elif no>arr1[mid]:
                high=mid-1
            else:
                return print("Roll Number is Present !")
        return print("Roll Number is not Present !")

    def Binary_Search2(self,arr,n,no,low,high): #recusrsive
        arr1=self.Bubble_Sort(arr,n)
        if low==high:
            if no==arr[low]:
                print("Roll Number is Present !")
        else:
            mid=(low+high)//2
            if arr1[mid]==no:
                print("Roll Number is Present !")
            elif no<arr1[mid]:
                return s.Binary_Search2(arr,n,no,mid+1,high)
            else:
                return s.Binary_Search2(arr,n,no,low,mid-1)
        print("Roll Number is not Present !")

    def FiboSearch(self,arr,n,no):
        arr1=self.Bubble_Sort(arr,n)
        a,b=0,1
        c=a+b
        offset=-1
        while c<n:
            a=b
            b=c
            c=a+b

        while c>1:
            i=min(offset+a,n-1)

            if arr1[i]<no:
                c=b
                b=a
                a=c-b
                offset=i
            elif arr1[i]>no:
                c=a
                b=b-a
                a=c-b
            else:
                return print("Roll Number is Present !")
        if b and arr1[n-1]==no:
            print("Roll Number is Present at ",n-1)
        else:
            print("Roll Number is not Present")

    def Partition(self,arr,low,high):
        pi=arr[high]
        i=low-1
        for j in range(low,high):
            if arr[j]<=pi:
                i=i+1
                arr[j],arr[i]=arr[i],arr[j]

        arr[high],arr[i+1]=arr[i+1],arr[high]
        return i+1

    def Quick_Sort(self,arr,low,high,n):
        i=n
        if low<high:
            loc=s.Partition(arr,low,high)
            s.Quick_Sort(arr,low,loc-1,n) #Before Pivot
            s.Quick_Sort(arr,loc+1,high,n) #After Pivot

    def Insertion_Sort(self,arr,n):
        for i in range(0,n):
            key=arr[i]
            j=i-1
            while j>=0 and arr[j]>key:
                arr[j+1],arr[j]=arr[j],arr[j+1]
                j=j-1
            arr[j+1]=key
        #print(arr)

    def Selection_Sort(self,arr,n):
        gap=n//2
        while gap>0: #for passes
            for i in range(gap,n):
                temp=arr[i]
                j=i
                while j>=gap and arr[j-gap]>temp:
                    arr[j]=arr[j-gap]
                    j=j-gap
                arr[j]=temp
            gap=gap//2

    def Quick(self,arr,low,high):
        if low>high:
            loc=s.Part(arr,low,high)
            s.Quick(arr,low,loc-1)
            s.Quick(arr,loc+1,high)

    def Part(self,arr,low,high):
        pi=arr[high]
        i=low-1
        for j in range(low,high):
            if arr[j]<=pi:
                i=i+1
                arr[i],arr[j]=arr[j],arr[i]
        arr[high],arr[i+1]=arr[i+1],arr[high]
        return i+1


s=AllSortSearch()
arr,n,nos=s.getInput()
#s.Binary_Search1(arr,n,nos)
#s.Binary_Search2(arr,n,nos,0,n-1)
#s.FiboSearch(arr,n,nos)
s.Quick_Sort(arr,0,n-1,n)
print(arr)
#s.Insertion_Sort(arr,n)
#print(arr)
#s.Insert(arr,n)
#print(arr)
#s.Quick(arr,0,n-1)
#print(arr)