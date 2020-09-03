import board
import digitalio
import time

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

#a simple test of the ability to load a program on the feather

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)