# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 15:10:46 2020

@author: dougb
"""

from math import pi

print("What is the radius of the sphere in cm?")

radius = float(input())

Volume = 4 * pi * (radius*3) / 3

print("Volume = " + str(Volume) + "cm^3")
