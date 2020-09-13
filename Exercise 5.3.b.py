# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 18:32:02 2020

@author: dougb
"""

def is_triangle_b(a,b,c):
    if a > b + c or b > a + c or c > a + b:
        print("No")
    else:
        print("Yes")

is_triangle_b(3,4,5)

