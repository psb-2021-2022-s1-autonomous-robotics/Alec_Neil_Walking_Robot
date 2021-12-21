# Add your Python code here. E.g. 
from microbit import *

#turn servo on pin to angle
def turn(pin, angle, cw, period=10):
    start = 0.55
    end = 2.3
    b = start
    m = (end - start) / 180
    t = m * angle + b
    pin.write_analog(t / period * 1023)
    #We used the angledjust the servo. When the angle is 0, the time is 0.55 ms. When the angle 180 the time is 2.3 ms.
    
    
pin15.set_analog_period(10)
pin16.set_analog_period(10)
while True:
    a=18
    turn(pin15, a, True)
    turn(pin16, a, True)
    sleep(1000)
    a=180
    turn(pin15, a, True)
    turn(pin16, a, True)
    sleep(1000)
    #this is the specific variables we are using to make it walk. Sleep is pause and a is the variable. Turn is the movement.
