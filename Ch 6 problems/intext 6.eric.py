# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 12:55:21 2020

@author: dbrown
"""

import math

point1 = [1,2]
point2 = [4,6]

def distance(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1
    print("dx is", dx)
    print("dy is", dy)
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

print(distance(point1[0],point1[1],point2[0],point2[1]))