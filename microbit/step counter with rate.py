# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 17:52:25 2020

@author: dougb
"""

from microbit import *

steps = 0

while True:

    if accelerometer.was_gesture("shake"):
        steps = steps + 1
        display.show(steps)

    if button_a.was_pressed():
        steps = 0
        display.show(steps)
        
    if button_b.was_pressed():
        rate = int(steps * 3600000 / running_time())
        display.scroll(rate)
        
