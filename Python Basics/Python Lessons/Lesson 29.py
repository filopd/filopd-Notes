# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 00:33:55 2019

@author: erpri
"""
print("""
1. Constructor:
    Python doesn't have explicit constructors like C++ or Java.
    __init__() method in Python is something similar as it is the first code which is executed, 
        when a new instance of a class is created.
    Wrong to call it a constructor, 
        because a new instance is already "constructed" by the time the method __init__ is called.
2. Destructor:
    There is no "real" destructor, but something similiar, i.e. the method __del__.
    Called when the instance is about to be destroyed.
      """)
