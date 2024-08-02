amt=int(input("Please enter the Salary :"))

if amt<=100000:
    print("No Tax")
elif amt>=100001 and amt<=150000:
    tax=(amt-100000)*10/100
    print("You need to pay Rs.",tax," on Rs.",amt)
elif amt>=150001 and amt<=250000:
    tax=5000+1(amt-150000)*20/100
    print("You need to pay Rs.",tax," on Rs.",amt)
else:
    tax=25000+(amt-250000)*30/100
    print("You need to pay Rs.",tax," on Rs.",amt)
