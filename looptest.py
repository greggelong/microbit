from microbit import *


def doA():
    while True:
        display.scroll("AaAaAa")

        if button_b.get_presses():
            break



def doB():
    while True:
        display.scroll("BbBbBb")

        if button_a.get_presses():
            break




while True:
    display.scroll("A or B")
    if button_a.get_presses():
        display.show(Image.ANGRY)
        sleep(200)
        doA()

    elif button_b.get_presses():
        doB()
