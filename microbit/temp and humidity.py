# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 17:47:53 2020

@author: dougb
"""

from microbit import *
import am2320

i2c.init(sda=pin15, scl=pin13)
sensor = am2320.AM2320(i2c)

while True:
	if button_a.is_pressed():
		try:
			sensor.measure()
			display.scroll(str(sensor.temperature())+"c", 150)
		except OSError:
			display.scroll("Err")
	if button_b.is_pressed():
		try:
			sensor.measure()
			display.scroll(str(sensor.humidity())+"%", 150)
		except OSError:
			display.scroll("Err")