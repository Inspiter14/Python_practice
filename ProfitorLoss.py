from socket import INADDR_LOOPBACK


cp=float(input("Enter the Cost Price of the Product in Rs: "))
sp=float(input("Enter the Selling Price of the Product in Rs: "))

if sp>cp:
    pp=((sp-cp)*100)/cp
    print("You are in Profit with ",pp,"%")
elif sp==cp:
    print("You have No Profit/No Loss")
else:
    lp=((cp-sp)*100)/cp
    print("You are in Loss with ",lp,"%")

