# -*- coding: utf-8 -*-
"""
Created on Mon May 28 15:20:00 2018

@author: erpri
"""
#Built-In Types: Simple Values
#int x = 1 Integers (i.e., whole numbers) 
#float x = 1.0 Floating-point numbers (i.e., real numbers) 
#complex x = 1 + 2j Complex numbers (i.e., numbers with a real and imaginary part) 
#bool x = True Boolean: True/False values 
#str x = 'abc' String: characters or text 
#NoneType x = None Special object indicating nulls
intX = 5
print("intX variable is of type", type(intX), "with value", intX)
#Integer in Python don't overflow just like other languages.
intY = 5 ** 100
print("intY is intX ** 100", intY)
#Integer division upcast to floating type of result. Usually other languages return int.
print("5 / 2 =", 5 / 2)
#Integer's floor division results to integer.
print("5 // 2 =", 5 // 2)
floatX = 3.145
floatY = 0.2e-2
floatZ = 0.2e2
print("Values of floatX, floatY & floatZ are", floatX , floatY , "&",floatZ)
floatX = float(intX)
floatY = float(3)
print("Values of floatX & floatY are", floatX , "&",floatY)

floatA = 0.12345698745
print(floatA)
print("{0:0.1f}".format(floatA))
print("{0:0.2f}".format(floatA))
print("{0:0.3f}".format(floatA))
print("{0:0.4f}".format(floatA))
print("{0:0.5f}".format(floatA))
#This is how it is going to be rounded.
print("0.1+0.2 == 0.3 ", (0.1+0.2)==0.3, "because, 0.1+0.2 =", 0.1+0.2)

