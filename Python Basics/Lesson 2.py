# -*- coding: utf-8 -*-
"""
Created on Sun May 27 18:48:09 2018

@author: erpri
"""
#This lesson is for Basic Python Semantics: Operators.
#a + b Addition Sum of a and b 
#a - b Subtraction Difference of a and b 
#a * b Multiplication Product of a and b 
#a / b True division Quotient of a and b 
#a // b Floor division Quotient of a and b, removing fractional parts 
#a % b Modulus Remainder after division of a by b 
#a ** b Exponentiation a raised to the power of b 
#-a Negation The negative of a 
#+a Unary plus a unchanged (rarely used)

#lets fo it !
a = 5; b = 3
print(" a is ", a , "& b is", b,".")
print("a + b", a + b)
print("a - b", a - b)
print("a * b", a * b)
print("a / b", a / b)
print("a // b", a // b)
print("a % b", a % b)
print("a ** b", a ** b)

#let's see the Unary Operators
print("Negation of a (", a,") is ", -a)
print("Negation of a (-", a,") is ", -(-a))
print("Unary of a (", a, ") is ", +a)
print("Unary of a (-", a, ") is ", +(-a))
c = 3.3111111152111111111116666666666666663333333333
print("c is ", c)
print("Unary of a (", c, ") is ", +c)

#Let's see the BDMAS priority
print("a+a-a/a*a//a%a", a+a-a/a*a//a%a)
print("a(",a,") / b(,", b,") : ", a/b,"a // b : ", a//b)
print("Compare / with // : ", a/b//b)
#If we see the result is 0.0. Means last action happened is definately is True Division.00


