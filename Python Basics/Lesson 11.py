# -*- coding: utf-8 -*-
"""
Created on Tue May 29 00:54:07 2018

@author: erpri
"""
#Sets: Same as list and tuples but curly braces like dictionaries.
#These are like mathematic's set only. It is having utitlites such as
# union, intersection, difference, symmetric difference
aSet = {1,2,3,7,8,9}
bSet = {1,4,7,3,6,9}
print("aSet is", aSet, "and bSet is",bSet)
print("Union is set of items appearing in any set", aSet | bSet)
print("Union is set of items appearing in any set", aSet.union(bSet))
print("Intersection is set of items appearing in both", aSet & bSet)
print("Intersection is set of items appearing in both", aSet.intersection(bSet))
print("Differene is set of items appearing in only 1st", aSet - bSet)
print("Differene is set of items appearing in only 1st", aSet.difference(bSet))
print("Differene is set of items appearing in only 2nd", bSet - aSet)
print("Differene is set of items appearing in only 2nd", bSet.difference(aSet))
print("Symmetric Differene is set of items appearing in only one set", bSet ^ aSet)
print("Symmetric Differene is set of items appearing in only one set", bSet.symmetric_difference(aSet))
