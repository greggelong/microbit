from microbit import *
import random

x = 0
y = 0


while True:
    display.set_pixel(x,y,9)
    sleep(250)
    if x < 4 and y < 4:
        a = random.randint(0,1)
        if a == 0:
            x=x+1

        else:
            y=y+1


    elif x == 4 and y < 4:
        y=y+1


    elif y == 4 and x <4:
        x=x+1



    else:
        display.clear()
        x=0
        y=0

