# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 16:28:00 2020

@author: dougb
"""

def count(whole,part):    

    amount = 0
    for letter in whole:
        if letter == part:
            amount = amount + 1
    print(amount)

count("watermelon", "e")
