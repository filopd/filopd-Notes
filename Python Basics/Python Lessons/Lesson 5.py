# -*- coding: utf-8 -*-
"""
Created on Mon May 28 14:38:58 2018

@author: erpri
"""
#Identity and Membership Operators.
#a is b True if a and b are identical objects 
#a is not b True if a and b are not identical objects 
#a in b True if a is a member of b 
#a not in b True if a is not a member of b
a = [1,2,3]
b = [1,2,3]
c = a
#Identity Operator: This is use to compare objects. As we have see before, objects are different
#than values. Ex. if we define variables like a = 1; b=1. Though the value is same but the object
#is different. In short 2 buckets with same value and different pointers. == is not same as "is".
print(" a is", a, ", b is ", b, " & c is", c)
print("a == b", a == b)
print("a is b", a is b)
print("a is c", a is c)
#Here in above example, when we assigned c = a, then same pointer i.e. same object is assigned.
print("a != b", a != b)
print("a is not b", a is not b)
print("a is not c", a is not c)

#Membership Operator: This operator will check whether particular value is present in the list 
#or not.
print("1 in a", 1 in a)
print("5 in a", 5 in a)
print("5 not in a", 5 not in a)
print("1 not in a", 1 not in a)
