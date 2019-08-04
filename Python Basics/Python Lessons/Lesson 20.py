# -*- coding: utf-8 -*-
#Lesson 20: Iterator Types
#Enumerators
print("----------------------Enumerator-----------------")
varL = [5,6,8,2,7,3]
print("List varL is", varL, " and length is ", len(varL))
for varI in range(len(varL)):
    print(varI, "*", varL[varI])
print("Here enumerate is:")
for varM, varN in enumerate(varL):
    print(varM, "+", varN)
print("----------------------Zip-----------------")
#Zip: Iterate 2 tables together. Length of list can be diff. Shortes will be outside loop.
varK = [1,5,2,3,4,7]
print("List varK is", varK, " and length is ", len(varK))
for varM, varN in zip(varK,varL):
    print(varM, "&", varN)
print("------------------MAP-----------------")
#Map: Iterate the value as a result of function having input from range.
#First define a normal funcion (any def or lambda)
def fun1(varIp):
    return varIp **2
print("List varL is", varL)
for varI in map(fun1, varL):
    print(varI)
print("------------------FILTER-----------------")
#Filter: Iterate the value from range if retun of function is true.
#First define a lambda.
is_odd = lambda varIp1 : varIp1 % 2 == 1
print("List varK is", varK)
for varI in filter(is_odd, varK):
    print(varI)


