# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 17:24:14 2020

@author: dougb
"""

def remainder(a,b):
    if abs(a / b) > 1:
        return (a - (int(a / b) * b))
    if abs(a / b) < 1:
        return remainder(b,a)
    #simply determines the remainder of any division problem

def gcd(a,b):
    if a == 0:
        return b
    if b == 0:
        return a
    # deals with division by 0
    if remainder(a,b) == 0 and a >= b:
        return b
    if remainder(a,b) == 0 and a < b:
        return a
    # returns the gcd if one term is an integer multiple of the other
    if remainder(a,b) != 0 and remainder(b , remainder (a,b)) == 0:
        return remainder(a,b)
    if remainder(a,b) != 0 and remainder(b , remainder (a,b)) != 0:
        return gcd(b , remainder (a,b))

print(abs(gcd(0.75,3.25)))

