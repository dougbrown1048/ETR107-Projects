# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 17:17:37 2020

@author: dougb
"""
space = " "

def right_justify(s):
    print(space * (70 - len(s)) + s)

right_justify("monty")
