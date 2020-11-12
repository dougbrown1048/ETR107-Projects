from microbit import *

pin16.write_digital(0) #make sure light is off/no pulse
sleep(1000)

while True:
    position = pin1.read_analog() #read the raw value off analog pin
    pin16.write_analog(position) #use that value to pulse PWM to change brightness of LED on output