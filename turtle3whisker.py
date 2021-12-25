# Write your code here :-)
from microbit import *
'''
 turtle3whisker.py
  this code works to simply move forward continuously until
  the whisker is triggered  then moves backwards and right around 180 degrees

  I killed a microbit (the blue one )  shorting out when hooking up the power

  really stupid mistake.

  the motor controller seems to work but it doesn't send power to the microbit as it did before

  it now only sends power to the motors

  I have to hook up a separate 3v for the microbit to get it to work see video

  I will have to do this with an Arduino and try not to short that out

  '''

def fward():
    """
    now swiched for new chassis
    backwards movement

    orientation
    motor connentions to outside
    motor to front gears box to back
    left side notch negitive up
    right side notch negative down
    """

    pin1.write_analog(300)  # speed control for a1 and a2
    pin13.write_digital(1)  # a1
    pin12.write_digital(0)  # a2

    pin2.write_analog(300)  # speed control for b1 and b2

    pin15.write_digital(1)  # b1
    pin16.write_digital(0)


def bwards():
    """
    now swiched for new car chassis
    forwards movement

    orientation
    motor connentions to outside
    motor to front gears box to back
    left side notch negitive up
    right side notch negative down
    """

    pin1.write_analog(300)  # speed control for a1 and a2
    pin13.write_digital(0)  # a1
    pin12.write_digital(1)  # a2

    pin2.write_analog(300)  # speed control for b1 and b2

    pin15.write_digital(0)  # b 1
    pin16.write_digital(1)  # b2

    sleep(200)


def lt():

    pin1.write_analog(500)  # speed control for a1 and a2
    pin13.write_digital(1)  # a1
    pin12.write_digital(0)  # a2

    pin2.write_analog(500)  # speed control for b1 and b2

    pin15.write_digital(0)  # b1
    pin16.write_digital(1)  # b2

    sleep(200)


def rt():

    pin1.write_analog(500)  # speed control for a1 and a2
    pin13.write_digital(0)  # a1
    pin12.write_digital(1)  # a2

    pin2.write_analog(500)  # speed control for b1 and b2

    pin15.write_digital(1)  # b1
    pin16.write_digital(0)  # b2

    sleep(200)


while True:
    pin14.write_digital(1)
    if pin0.read_digital() == 1:
        display.show(Image.ANGRY)
        bwards()
        rt()
        rt()
    else:
        pin1.write_analog(300)  # speed control for a1 and a2
        pin13.write_digital(1)  # a1
        pin12.write_digital(0)  # a2

        pin2.write_analog(300)  # speed control for b1 and b2

        pin15.write_digital(1)  # b1
        pin16.write_digital(0)

        display.show(Image.SAD)
