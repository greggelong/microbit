from microbit import *
ldr1 = 0
ldr2 = 0
uart.init(115200)
pin14.write_digital(1)

def vehicle2b():
    while True:
        #  can't seem to read buttons to break out just use reset button

        display.off()

        ldr1 = pin0.read_analog()  # read the ldrs
        ldr2 = pin3.read_analog()
        sleep(200)
        uart.write(str(ldr1) + "   " + str(ldr2)+"\n")
        pin1.write_analog(ldr1)  # speed control for a1 and a2
        pin13.write_digital(0)  # a1
        pin12.write_digital(1)  # a2

        pin2.write_analog(ldr2)  # speed control for b1 and b2

        pin15.write_digital(0)  # b 1
        pin16.write_digital(1)  # b2


while True:
    display.scroll("Press A to start")
    if button_a.was_pressed():
        display.show(Image.ANGRY)
        sleep(200)
        vehicle2b()