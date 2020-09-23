# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 18:35:34 2020

@author: dougb
"""

def do_twice(this, that):
    this(that)
    this(that)

def print_twice(that):
    print(that)
    print(that)

do_twice(print_twice, "spam")
