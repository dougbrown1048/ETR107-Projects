# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 16:23:33 2020

@author: dougb
"""

print("What is the cover price of the book?")

price = float(input())

discountPrice = price * .6

print("How many copies do you want?")

copies = int(input())

shipping = 3 + (copies - 1) * .75

print("Your total cost is $" + str(discountPrice + shipping))
