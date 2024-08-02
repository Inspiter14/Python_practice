def sort(arr,nos):
    i=0
    j=0
    temp=0
    for i in range(nos-1):
        for j in range(nos-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    #print(arr)
    
def Bsearch(arr,n,x): #Iterative
    sort(arr,nos)
    low=0
    high=n-1
    mid=0
    while low <= high:
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return print("Found at",mid,"th pos")
    return print("Not Found")

def Bsearch1(arr,x,low,high,nos):  #Recursive
    sort(arr,nos)
    mid=0
    if low==high:
        if arr[low]==x:
            return print("Found at",low,"th pos")
        return print("Not Found")
    else:
        mid=(low+high)//2
        if arr[mid]==x:
            return print("Found at",mid,"th pos")
        elif x<arr[mid]:
            Bsearch1(arr,x,low,mid-1,nos)
        else:
            Bsearch1(arr,x,mid+1,high,nos)
            

def getInput():
    l1=[]
    n=int(input("Enter how many elements you want to insert:"))
    for i in range(0,n):
        ele=int(input("Enter the element:"))
        l1.append(ele)
    #print(l1)
    num=int(input("Enter the element to be searched"))
    return l1,n,num

a1,nos,search=getInput()
#Bsearch(a1,nos,search)
low=0
high=nos-1
Bsearch1(a1,search,low,high,nos)
    
    
