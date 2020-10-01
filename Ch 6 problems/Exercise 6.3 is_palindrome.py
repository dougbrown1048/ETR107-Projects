# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 16:21:47 2020

@author: dougb
"""


def first(word):
    return word [0]

def last(word):
    return word [-1]
    
def middle(word):
    return word [1:-1]

def isPalindrome(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return isPalindrome(middle(word))

print(isPalindrome("redivider"))

