# -*- coding: utf-8 -*-
"""
Created on Mon May 28 21:58:57 2018

@author: erpri
"""
#Build-In Data Structures: list
aList = [9,6,5,4,8]
print("List aList is", aList)
print("Lenght of aList is", len(aList))
print("Append 5 into list aList", aList.append(5), aList)
print("Concatenate [22,11] into aList then it is",aList+[22,11], aList)
aList = [9,6,"LOL",8]
print("List aList is", aList)
#Let's sort this list now. Need to keep same type of objects.
aList = [9,6,55,8]
aList.sort()
print("Sorted list aList is", aList)
print("##########################")
#List indexing and slicing 
bList = [5,8,3,4,7,0,9]
print("New List bList", bList)
print("##########################")
#Access one element of list
print("1st value of bList", bList[0])
print("Last value of bList", bList[-1])
bList[-2]=100
print("Assign 100 to the 2nd last value of bList", bList)
print("##########################")
#let's slice the list in some ways
print(" 2nd to 4th of bList is", bList[1:4])
print(" 2nd to 2nd Last of bList is", bList[1:-1])
print("##########################")
print(" 1st to 4th of bList is", bList[:4])
print(" 4th to last of bList is", bList[3:])
print("##########################")
print(" Elements step by step of 1 of bList is", bList[::1])
print(" Elements step by step of 2 of bList is", bList[::2])
print(" Elements step by step of 3 of bList is", bList[::3])
print("##########################")
print(" Elements reverse step by step of 1 of bList is", bList[::-1])
print(" Elements reverse step by step of 2 of bList is", bList[::-2])
print(" Elements reverse step by step of 3 of bList is", bList[::-3])
print("##########################")
