# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 18:35:34 2020

@author: dougb
"""

def do_twice(f):
    f()
    f()

def print_spam():
    print("spam")

do_twice(print_spam)
