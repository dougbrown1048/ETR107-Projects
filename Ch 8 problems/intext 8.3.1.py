# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 18:39:25 2020

@author: dougb
"""

fruit = "pineapple"

index = -1

while abs(index) <= len(fruit):
    letter = fruit[index]
    print(letter)
    index = index - 1

