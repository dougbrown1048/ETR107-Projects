# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 16:06:57 2020

@author: dougb
"""

def palindrome(word):

    def first(word):
        return word [0]
    
    def last(word):
        return word[-1]
        
    def middle(word):
        return word [1:-1]

    print(first(word))
    print(last(word))
    print(middle(word))
    
palindrome("frank")

