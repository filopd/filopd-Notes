# -*- coding: utf-8 -*-
"""
Created on Sun May 27 17:58:44 2018

@author: erpri
"""
#Assignments of values to Variables is nothing but assigning the pointers of Bucket.
intX = 5
#here 5 is value in some bucket and pointer to this bucket is assigned to variable intX.
print("intX is pointing to bucket having", intX, ".")
intY = intX
print("intY is pointing to bucket having", intY, ".")
intX = 5+5
print("intX is pointing to bucket having", intX, ".")
print("intY is pointing to bucket having", intY, ".")
#Here if you see, the value of intX is pointed to another new bucket with value 5+5.
#But still the value of intY is pointing to old bucket pointer.
intY = "This is new"
print("intY is now ", intY)
intY = "4.5"
print("intY is now ", intY)
#this is nothing but example that Python is OOriented and Type-Less.
#In Python, every thing is Object Oriented.
#1.Object = Entity
#2.Metadata = Attributes
#3.Functions = Methods
#let's take an example of simple variable.
intObject = 4.5
print("4.5 has Imaginary part ",intObject.imag," and real part", intObject.real)
#This is nothing but Metadata or Attributes of Variable intObject.
print("4.5 is Integer ? ",intObject.is_integer())
#This is nothing but Functions or Methods of Variable intObject.
