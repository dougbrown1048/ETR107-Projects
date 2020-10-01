# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 17:02:26 2020

@author: dougb
"""

def is_power(a,b):
    if a/b == 1:
        return True
    if a/b == int(a/b):
        return is_power(a/b,b)
    else:
        return False

print(is_power(27,3))
