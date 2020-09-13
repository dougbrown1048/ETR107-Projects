# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 18:45:36 2020

@author: dougb
"""

def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)
        
recurse(3,5)

# this function will only work for values of n => zero