
from microbit import *
import am2320

while True:
	if button_a.is_pressed():
		display.scroll(str(running_time())+"us", 150)