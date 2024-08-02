#Insertion Sort
'''def Insertion(a,size):
    for i in  range(1,size):
        item=a[i]
        j=i-1
        while j>=0 and item<a[j]:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=item

Insertion(a,size)
print(a)'''
a=[3,1,6,7]
size=len(a)

#Shell(a,size)
def Shell(a,size):
    gap=size//2
    #temp=0
    while gap>0:
        j=gap
        while j<= size-1:
            i=j-gap
            while i>=0:
                if a[i+gap]>a[i]:
                    break
                else:
                    temp = a[i + gap]
                    a[i + gap] = a[i]
                    a[i] = temp
                print(i)
                i=i-gap
                
        j=j+1
    gap=gap//2
    

Shell(a,size)    


    
