# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 16:17:34 2020

@author: dougb
"""

from microbit import *

steps = 0

while True:

    if accelerometer.was_gesture("up"):
        steps = steps + 1
        display.show(steps)

    if button_a.was_pressed():
        steps = 0
        display.show(steps)
        
    if button_b.was_pressed():
        display.scroll(steps)
        
