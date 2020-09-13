# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 18:16:26 2020

@author: dougb
"""

import math

def check_fermat(a,b,c,n):
    x = a ** n + b ** n
    y = c ** n
    if x == y:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work")
             
check_fermat(3,4,5,2)
