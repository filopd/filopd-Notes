# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 00:17:07 2019

@author: erpri
@ Inheritance:
    creating new class for using details of existing class without modifying it
    New class is Child Class and existing class is Parent Class.
@ Example 3: Use of Inheritance in Python
"""

# parent class
class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        # to pull the content of __init__() method from the parent class into the child class
        # Used super() before __init__()
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()