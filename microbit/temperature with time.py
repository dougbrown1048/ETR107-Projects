# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 17:47:53 2020

@author: dougb
"""

from microbit import *
import am2320


# function to retrieve the temperature data in the text file
def get_temperature(name):
    with open(name) as file:
        value = float(file.read())
    return value

# function to retrieve the time data in the text file
def get_time(name):
    with open(name) as file:
        value = float(file.read())
    return value

# function to save the temperature data in the text file
def set_temperature(name, value):
    with open(name, 'w') as file:
        file.write(str(value))

# function to save the time data in the text file
def set_time(name, value):
    with open(name, 'w') as file:
        file.write(str(value))

i2c.init(sda=pin15, scl=pin13)
sensor = am2320.AM2320(i2c)

while True:
    if button_a.is_pressed():
        sensor.measure()
        display.scroll(str(sensor.temperature())+"c", 150)
        set_temperature('temp.txt', str(sensor.temperature()))
        set_time('time.txt', str(running_time()))
    if button_b.is_pressed():
        display.scroll(str(get_temperature('temp.txt'))+"c", 150)
        display.scroll(str(get_time('time.txt'))+"us", 150)
