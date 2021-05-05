from microbit import *
from machine import time_pulse_us
ldr1 = 0
ldr2 = 0
# having power troubles
# must turn off all the uart stuff
# choose pins based on wiring


# uart.init(115200)
pin14.write_digital(1)


def bwards(speed, tm):
    '''
        backwards movement
        for avoidance

        orientation
        motor connentions to outside
        motor to front gears box to back
        left side notch negitive up
        right side notch negative down
    '''

    pin1.write_analog(speed)  # speed control for a1 and a2
    pin13.write_digital(1)  # a1
    pin12.write_digital(0)  # a2

    pin2.write_analog(speed)  # speed control for b1 and b2

    pin15.write_digital(1)  # b1
    pin16.write_digital(0)

    sleep(tm)

def rt():

    pin1.write_analog(500)  # speed control for a1 and a2
    pin13.write_digital(0)  # a1
    pin12.write_digital(1)  # a2

    pin2.write_analog(500)  # speed control for b1 and b2

    pin15.write_digital(0)  # b1
    pin16.write_digital(0)  # b2

    sleep(1400)

def avoidance():
    display.off()
    trig = pin7
    echo = pin6
    # set up IO
    trig.write_digital(0)
    echo.read_digital()
    # trigger ultrasonic burst
    trig.write_digital(1)
    trig.write_digital(0)
    # measure the input echo puls in microseconds and covets to seconds
    micros = time_pulse_us(echo, 1)
    t_echo = micros / 1000000
    # caculate distanced
    distancecm = (t_echo / 2) * 34300
    # uart.write(str(distancecm)+"\n")
    if distancecm < 8:

        bwards(500, 1000)
        rt()



def vehicle2b():
    while True:
        #  can't seem to read buttons to break out just use reset button

        display.off()
        #  call the function to check


        ldr1 = pin0.read_analog()  # read the ldrs  yellow wire
        ldr2 = pin3.read_analog()  #orange wire
        sleep(200)

        pin1.write_analog(ldr1)  # speed control for a1 and a2
        pin13.write_digital(0)  # a1
        pin12.write_digital(1)  # a2

        pin2.write_analog(ldr2)  # speed control for b1 and b2

        pin15.write_digital(0)  # b 1
        pin16.write_digital(1)  # b2
        avoidance()


while True:
    display.scroll("Press A to start")
    if button_a.was_pressed():
        display.show(Image.ANGRY)
        sleep(200)
        vehicle2b()