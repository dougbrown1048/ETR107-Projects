# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 18:39:25 2020

@author: dougb
"""

prefixes = "JKLMNOPQ"

suffix = "ack"

for letter in prefixes:
    if letter == "Q" or letter == "O":
        print(letter + "u" + suffix)
    else:
       print(letter + suffix)
