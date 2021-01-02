# tinybit ultrasonic using firialabs.com/blogs
#  bread board and clips board with sound
# I have also rewired the breakout board using the pin map
# https://makecode.microbit.org/device/pins
# https://firialabs.com/blogs/lab-notes/ultrasonic-distance-sensor-with-python-and-the-micro-bit


from microbit import *
from machine import time_pulse_us
import music

# choose pins based on wiring
trig = pin2
echo = pin1
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

    # trigger ultrasonic burst
    trig.write_digital(1)
    trig.write_digital(0)
    # measure the input echo puls in microseconds and covets to seconds
    micros = time_pulse_us(echo, 1)
    t_echo = micros / 1000000
    # caculate distanced
    distancecm = (t_echo / 2) * 34300
    if distancecm < 55:
        mypich = mapVal(distancecm, 2, 55, 261, 523)  # from 2 to 55 cm from c4 to c5 note freq
        music.pitch(int(mypich), -1)
        print(distancecm, mypich)
        display.show(Image.MUSIC_QUAVER)

    else:
        music.pitch(0, -1)
        display.show(Image.NO)
    sleep(200)