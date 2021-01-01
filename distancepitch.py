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

while True:

    # trigger ultrasonic burst
    trig.write_digital(1)
    trig.write_digital(0)
    # measure the input echo puls in microseconds and covets to seconds
    micros = time_pulse_us(echo, 1)
    t_echo = micros / 1000000
    # caculate distanced
    distancecm = (t_echo / 2) * 34300
    # display.scroll(int(distancecm))
    print(distancecm)
    music.pitch(int((distancecm))+261,-1)
    '''
    if distancecm < 25:
        display.show(Image.SAD)
        # music.play("C4:4")
    else:
        display.show(Image.HAPPY)
        # display.scroll(int(distancecm))
    '''
    sleep(200)