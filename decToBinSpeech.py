from microbit import *
import speech
# looks like speech sends a pulse to pin 1 so now useing pin 8
# import music

dly = 300
# set the pins for LEDS to show binary
# making sure not to use leads multi with mbit display
ones = pin12
twos = pin8
fours = pin2
eights = pin16

def dtob(n):
    b = []
    if n % 2 == 0:
        b.insert(0, 0)
    else:
        b.insert(0, 1)
    while(n > 1):
        n //= 2
        b.insert(0, n % 2)

    for i in range(4-len(b)):
        # add leading zero for four bit numbers
        b.insert(0, 0)

    return b


def main():

    for i in range(16):
        mybin = dtob(i)
        speech.say(str(i))
        # looks better if you turn on the LEDs first
        ones.write_digital(mybin[3])
        twos.write_digital(mybin[2])
        fours.write_digital(mybin[1])
        eights.write_digital(mybin[0])
        # speech.say(str(i))
        display.scroll(i)
        # speech and display enough display sleep(dly)
        ones.write_digital(0)
        twos.write_digital(0)
        fours.write_digital(0)
        eights.write_digital(0)
        sleep(dly)



while True:
    main()


