orgamt=int(input("Enter the original amount of the product: "))

dis=((orgamt*10)/100)
disamt=orgamt-dis
print("The Amount after calculating Discount is :",disamt)

tax=((disamt*6)/100)
famt=disamt+tax
print('The Final Amount of Produxt is: ',famt)