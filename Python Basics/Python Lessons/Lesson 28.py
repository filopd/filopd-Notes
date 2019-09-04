# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 00:27:47 2019

@author: erpri
@Polymorphism
    Ability to use common interface for multiple form (data types).
    To call same method defined for different classes.
#Example 5: Using Polymorphism in Python
"""
class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface: takes any object and call method in it.
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)
    