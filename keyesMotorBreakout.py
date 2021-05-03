from microbit import *

# need to turn this on
pin14.write_digital(1)


while True:

    '''
        backwards movement

        orientation
        motor connentions to outside
        motor to front gears box to back
        left side notch negitive up
        right side notch negative down
    '''

    pin1.write_analog(500)  # speed control for a1 and a2
    pin13.write_digital(1)  # a1
    pin12.write_digital(0)  # a2

    pin2.write_analog(500)  # speed control for b1 and b2

    pin15.write_digital(1)  # b1
    pin16.write_digital(0)  # b2


    sleep(3000)


    '''
        forwards movement

        orientation
        motor connentions to outside
        motor to front gears box to back
        left side notch negitive up
        right side notch negative down
    '''


    pin1.write_analog(500) # speed control for a1 and a2
    pin13.write_digital(0) #a1
    pin12.write_digital(1) #a2

    pin2.write_analog(500) # speed control for b1 and b2

    pin15.write_digital(0) #b1
    pin16.write_digital(1) #b2

    sleep(3000)
