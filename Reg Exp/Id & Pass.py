from re import *

uid=input("Enter the User ID: ")
pwd=input("Enter the Password: ")

if match("^DSE22\d",uid):
    print("User ID is Correct.")
else:
    print("Please enter valid data.")

if findall("\w\d\W",pwd):
    print("Password is Correct.")
else:
    print("Please enter valid data.")
