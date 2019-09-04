# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 00:23:43 2019

@author: erpri
@Encapsulation
    Restrict access to methods and variables to prevent data from direct modification.
    Denote private attribute using underscore as prefix i.e single "_" or double "__".
@Example 4: Data Encapsulation in Python
"""
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price): #setter function
        self.__maxprice = price

c = Computer()
c.sell()

# Try to change the price but no use
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()
