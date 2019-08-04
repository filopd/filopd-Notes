# -*- coding: utf-8 -*-
"""
Created on Sun May 27 21:56:04 2018

@author: erpri
"""
#Bitwise Oerations
#a & b Bitwise AND Bits defined in both a and b 
#a | b Bitwise OR Bits defined in a or b or both 
#a ^ b Bitwise XOR Bits defined in a or b but not both 
#a << b Bit shift left Shift bits of a left by b units 
#a >> b Bit shift right Shift bits of a right by b units 
#~a Bitwise NOT Bitwise negation of a
#First Convert the Integers into Binary
a = 3
b = 8
print("a is ", bin(a), "and b is", bin(b))
print("a & b ", bin(a & b))
print("a | b ", bin(a | b))
print("a ^ b ", bin(a ^ b))
print("a << b ", bin(a << 1))
print("a << b ", bin(a >> 1))
print("~a", bin(~ a))
