ldr2 = 0
ldr1 = 0
headAngle = 90
basic.show_icon(IconNames.ASLEEP)

def on_forever():
    global ldr1, ldr2, headAngle
    ldr1 = pins.analog_read_pin(AnalogPin.P1)
    ldr2 = pins.analog_read_pin(AnalogPin.P2)
    if ldr1 < ldr2 and headAngle < 175:
        headAngle += 5
        basic.show_icon(IconNames.HAPPY)
    elif ldr1 > ldr2 and headAngle > 5:
        headAngle += -5
        basic.show_icon(IconNames.SAD)
    serial.write_value("ldr1", ldr1)
    serial.write_value("ldr2", ldr2)
    serial.write_value("head", headAngle)
    servos.P0.set_angle(headAngle)
basic.forever(on_forever)