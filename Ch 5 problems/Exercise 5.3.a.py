# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 18:32:02 2020

@author: dougb
"""

def is_triangle_a(a,b,c):
    if a + b > c and b + c > a and a + c > b:
        print("Yes")
    else:
        print("No")

is_triangle_a(3,4,5)

