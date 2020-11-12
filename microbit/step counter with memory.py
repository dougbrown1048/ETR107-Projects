# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 18:18:04 2020

@author: dougb
"""

from microbit import *

steps = 0 #sets step to zero
delay = 1500 #delay between clearing led screen (ms)

# function to retrieve the data in the text file
def get_step_count(name):
    with open(name) as file:
        value = int(file.read())
    return value
    
# function to save the data in the text file
def set_step_count(name, value):
    with open(name, 'w') as file:
        file.write(str(value))

while True:
    
# when the device goes "up" -> adds a step, shows the steps, saves the new data into the text file, waits, then clears display
    if accelerometer.was_gesture("up"):
        steps += 1
        display.show(steps)
        set_step_count('counting.txt', steps)
        sleep(delay)
        display.clear()
        
# when a is pressed -> resets steps to zero, shows that value, waits, clears display
    if button_a.was_pressed():
        steps = 0
        display.show(steps)
        sleep(delay)
        display.clear()
  
# when b is pressed -> find the value stored in the text file and display it, wait, clear display
    if button_b.was_pressed():
        display.scroll(get_step_count('counting.txt'))
        sleep(delay)
        display.clear()
        