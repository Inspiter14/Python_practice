'''Importing module AddFun.py and using function add() from that
Ways to import a module and using it:
1. from module-name import * : it will import all the methods/fun/data members
                               to use w/o '.' operator as well as mod-name
2. import module-name : it will import all the methods/fun/data members to use
                        but need to use '.' operator as well as mod-name
3. import module-name as convinient-name-for-module : same as "2" but we can use
                        optional name of module
4. from module-name import fun1-name,fun2-name,etc : we can import specific functions and no need to use dot operator 
'''
'''
from AddFun import *
print("Addition is :")
add()
'''
'''
2:
import AddFun
print("Addition is :")
AddFun.add()

3:
import AddFun as af
print("Addition is :")
af.add()

4:'''
from AddFun import mul
print("Multiplication is :")
mul()



