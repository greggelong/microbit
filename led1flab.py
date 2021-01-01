from microbit import *

def main():

    pin0.write_digital(1)
    sleep(500)
    pin0.write_digital(0)
    sleep(500)
    pin1.write_digital(1)
    sleep(500)
    pin1.write_digital(0)
    sleep(500)
    pin2.write_digital(1)
    sleep(500)
    pin2.write_digital(0)
    sleep(500)
while True:
    main()