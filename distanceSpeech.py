from microbit import *
from machine import time_pulse_us
import speech


# choose pins based on wiring
# need to change the pins as speech is using pin one

trig = pin8
echo = pin2
# set up IO
trig.write_digital(0)
echo.read_digital()

def mapVal(n, a, b, c, d):
    '''
     recreating the map() function from p5
     with help from
     https://stackoverflow.com/questions/48802987/is-there-a-map-function-in-vanilla-javascript-like-p5-js/48803093#48803093
    '''
    n = (n-a)/(b-a)
    return c + n * (d-c)


while True:
    speech.say("Danger, ")

    # trigger ultrasonic burst
    trig.write_digital(1)
    trig.write_digital(0)
    # measure the input echo puls in microseconds and covets to seconds
    micros = time_pulse_us(echo, 1)
    t_echo = micros / 1000000
    # caculate distanced
    distancecm = (t_echo / 2) * 34300
    #display.scroll(str(round(distancecm,2)))
    speech.say(str(round(distancecm,2)))
    speech.say(", centemeters")

    ##sleep(200)  # Write your code here :-)
