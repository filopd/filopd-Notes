# -*- coding: utf-8 -*-
"""
Created on Tue May 29 00:12:02 2018

@author: erpri
"""
#Tuples: same as List but below 3 main difference.
#1. Instead of [] square brackets, use paranthesis.
#2. No need to use any brackets.
#3. Immutable list. Can not assign or append any new value.
#Mosty used to catch the multiple return types of functions.
aTuple = (6,4,8,2)
print("aTuple is", aTuple)
bTuple = 7,4,1,3,6,9
print("aTuple is", bTuple)
#Retrieval of value is same.
print("1st value of aTuple is", bTuple[0])
print("Last value of aTuple is", bTuple[-1])
#Multple reurn items
print("Numerator and denominator of 3.14444 are", 3.14444.as_integer_ratio())
#Let's catch the numerator and denominator.
nrInt, drInt = 3.14444.as_integer_ratio()
print("Denominator & Numerator of 3.14444 are", drInt,nrInt)
#On assignment, you will get this error.
bTuple[1]=5


