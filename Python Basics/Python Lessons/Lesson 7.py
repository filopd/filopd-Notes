# -*- coding: utf-8 -*-
"""
Created on Mon May 28 20:35:17 2018

@author: erpri
"""
#Complex Numbers
cmplx1 = 1+2j
print("Complex Number is ", cmplx1)
cmplx2 = complex(3,5)
print("Complex Number is ", cmplx2)
print("Real Numbers are", cmplx1.real, ",", cmplx2.real)
print("imaginary Numbers are", cmplx1.imag, ",",cmplx2.imag)
#String Type
aString = " heLLo dear !"
print("original string is", aString)
#access any character from the String.
print("0th Space, 1st h & last one:",aString[0],aString[1],aString[-1])
print("aString.capitalize is", aString.capitalize())
print("aString.casefold() is", aString.casefold())
print("aString.center is ", aString.center(1))
print("aString.find is", aString.find("!"))
print("aString.lower is", aString.lower())
print("aString.upper",aString.upper())
print("aString.title",aString.title())
print("Multiple aString.title X 5",aString.title()*5)

#None Type
bNone = None
print("Value of None type of Variable is ", bNone)

