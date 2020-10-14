# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 19:09:12 2020

@author: dougb
"""

def find(word , index, letter):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print(find("question" , 5 , "t"))
