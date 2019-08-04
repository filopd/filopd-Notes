# -*- coding: utf-8 -*-
#Lesson 18: Use of Iterator over lise.
#Range is not list but interator. Let's define an iterator.
for valA in [2,4,6,8,10]:
    print(valA , end= '-')
print("-------------")
vari = iter([2,4,6,8,10])
print(vari)
print(next(vari))
print(next(vari))
print(next(vari))
print(next(vari))
print(next(vari))
#Range()
print(range(5))
for varI in range(5):
    print(varI, end='*')

print(" Next is")
print(iter(range(5)))
for varI in iter(range(5)):
    print(varI, end='*')
print("-------------")
#itertools: this is library function, press Ctrl + C to stop this..
#from itertools import count
#for varJ in count():
#    if varJ>=10:
#        print(varJ, end = '-*-')
#    print(" | ",varJ,"|")
