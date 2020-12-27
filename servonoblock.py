from microbit import *
#servo dosent work
pin0.set_analog_period(20)

def main():
    while True:
        pin0.write_analog(1023*1/20)
        display.scroll("hi")
        sleep(2050)
        pin0.write_analog(1023*2/20)
        display.scroll("by")
        sleep(2050)
        pi

main()