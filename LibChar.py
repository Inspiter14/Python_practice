ans=input("Are You Submitting Book late ? [Please type Y/y or N/n]: ")

if ans=="y" or ans=="Y":
    days=int(input("Please enter no of days that you are submitting late: "))
    if days<=5:
        ch=40*days
    elif days>5 and days<=10:
        ch=(5*40)+((days-5)*65)
    else:
        ch=(5*40)+(10*65)+(80*(days-10))
       
else:
    print("You don't need to pay Late Fees. Thank You ")