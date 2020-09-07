# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 12:51:36 2020

@author: dougb
"""

import random

print ("Pick a number between 1 and 10")
guess = int(input())
randNum = random.randint(1,10)

def randomNumFunc():
    if guess == randNum:
        print ("That's right!")
    if guess < randNum:
        print ("Sorry, too low. The actual number was "+ str(randNum) +".")
    if guess > randNum:
        print ("Sorry, too high. The actual number was "+ str(randNum) +".")

randomNumFunc()
