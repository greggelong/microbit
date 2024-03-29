# microbit and Arduino
a place to hold micro bit scripts

## Dec 27 2020

## ultrasonic sensor

I have rewritten the the script using only micropython and microbit library.
follwing the tutorial at # tinybit ultrasonic using firialabs.com/blogs

connection:
bread board and clips board with sound
I have also rewired the breakout board using the pin map

I am trigering with pin 2 and getting the echo with pin 1
Then using pin0 for sound

using the breadboad and breakout board to connect

https://makecode.microbit.org/device/pins

https://firialabs.com/blogs/lab-notes/ultrasonic-distance-sensor-with-python-and-the-micro-bit

## Jan 11th 2021

### decToBinSpeech2.py
### dectoBinSpeech3.py (added number words for teens)
(improved dtob(n) function)

While working with LEDs, breadboards and circuits while studying basic electronics on the Arduino
I made a quick project to visualize four bit Binary and Decimal numbers with the microbit.
I am using a break out board and 330 ohm resistors and 5mm leds.  they are still bright considering
they are being powerd only my microbit 3v. They are 5v on the arduino.

I am using the break out board and chose pins that are not already coupled to the microbits led matrix

 set the pins for LEDS to show binary
 
 making sure not to use leads multi with mbit display 
 
ones = pin12

twos = pin8

fours = pin2

eights = pin16

I am also using speech to say the numbers

speech sends a pulse to pin one so you must avoid that one too.

also there is some bleed if pin2 is on while speech.say is called

the led will flicker.

I have just timed it so that does not happen

I wrote my own decimal to binary conversion using the division by 2 method

my first attempt had an extra step (but still worked). but I improved it after doing it on paper.

```Python

def dtob(n):
    b = []
    # b is a list of binary conversion 9 = [1,0,0,1]
    # I use the ones and zeros to on pin.write_digital(b[index])

    while(n >= 1):
        # first insert remainder after divison
        b.insert(0, n % 2)
        # then do floor divison by 2
        n //= 2
        
    for i in range(4-len(b)):
        # add leading zero for four bit numbers
        b.insert(0, 0)
        
    return b
    
   ```
I take a look at dectobindisplay1 for arduino

you can see the way i had to implement it.

The arrays are less cooperative in c type languages returning them from a function
involves malock and all sorts of other things.  so just did it in the main loop. with help
from some posts.
I find arduino c type language much less flexible than micropython.
However as for hooking up hardware it is much easier.  


# Feb 22 2021

I am using two microbits connected by radio to send Serial data to a processing sketch

the sender sends  a string by radio:

a L if tilted left

a R if tiltled right

and an N if not tilted


the receiver which is connected by usb to the computer 

sends a string over the serial port to the processing sketch.

The processing sketch reads the string over the serial and checks the

charAt(0) if that char is L it moves a ball left 

if it is R it moves a ball right

if N  the ball is not moved.

code for reciever in python microbit make code

```Python

def on_received_string(receivedString):
    led.toggle(4, 0)
    basic.show_string(receivedString)
    serial.write_string(receivedString)
radio.on_received_string(on_received_string)

radio.set_group(1)

```

code for sender in python mocrobit make code

```Python

basic.show_icon(IconNames.ASLEEP)
radio.set_group(1)

def on_forever():
    led.toggle(0, 0)
    if input.is_gesture(Gesture.TILT_LEFT):
        radio.send_string("L")
    elif input.is_gesture(Gesture.TILT_RIGHT):
        radio.send_string("R")
    else:
        radio.send_string("N")
basic.forever(on_forever)




```
# Feb 26 2021

using microbit with 2 LDRs and Servo 

https://www.youtube.com/watch?v=-7wrmRCEnB0

and reading the LDRs ananlog input values with serial on a linux terminal.


I am in total using three pins + 3.3v and ground on the microbit.

pin 1 and pin 2 are anolog input pins for getting values from LDRs

the value is read from a point between LDR leg and a 5k resistor

like my other LDR circuits in ardiuino

pin0 is ouput for the 180 degree servo. using the servo library from makecode

the program works by reading the values of the LDRs then

then moving the servo toward the drection of most light (highest value)

ldrServoMbit.py

ldrServoMbit.hex

```Python
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

```

using the serial is easy if screen is on linux

Find which device node the micro:bit was assigned to with the command ls /dev/ttyACM*.

If it was /dev/ttyACM0, type the command screen /dev/ttyACM0 115200


# May 3rd  Keyes dc motor breakout board

I ordered a Keyes breakout board from TaoBao

The chinese company has a little info on their website

it is not well documented and it is in Chinese

but there is enough info to get it to work with some

playing around.

see the documentation at

https://www.keyesrobot.cn/KE0136/

The result of my playing around is the following functions

to move a turtle like car

This code is micropython not makecode python

```Python
def bwards(speed, tm):
    ''' 
        backwards movement
        
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

    
def fward(speed, tm):
    ''' 
        forwards movement
        
        orientation 
        motor connentions to outside
        motor to front gears box to back
        left side notch negitive up 
        right side notch negative down
    ''' 

    pin1.write_analog(speed)  # speed control for a1 and a2
    pin13.write_digital(0)  # a1 
    pin12.write_digital(1)  # a2

    pin2.write_analog(speed)  # speed control for b1 and b2

    pin15.write_digital(0)  # b 1
    pin16.write_digital(1)  # b2

    sleep(tm)

def lt():

    pin1.write_analog(500)  # speed control for a1 and a2
    pin13.write_digital(0)  # a1 
    pin12.write_digital(0)  # a2

    pin2.write_analog(500)  # speed control for b1 and b2

    pin15.write_digital(0)  # b1
    pin16.write_digital(1)  # b2

    sleep(700)

def rt():

    pin1.write_analog(500)  # speed control for a1 and a2
    pin13.write_digital(0)  # a1 
    pin12.write_digital(1)  # a2

    pin2.write_analog(500)  # speed control for b1 and b2

    pin15.write_digital(0)  # b1
    pin16.write_digital(0)  # b2

    sleep(700)



```
# May 3rd Light dependant resistors and micropython

will incorporate two LDRs to seek light with the turtle car

to make a Braitenberg vehicle

I was thinking I could just as defalt go forward at a slow speed 

and map the speed of each wheel to how much light it is getting

if the right eye senses the light

the left wheel should speed up to turn into the light

and if the left eye senses 

the right wheel should go faster to turn into the light


a light avoiding vehicle would do just the opposite

to use ldrs with micropython  see this script

```Python
from microbit import *

ldr1 = 0

uart.init(115200)

while True:
    
    ldr1 = pin1.read_analog()
    display.scroll(ldr1)
    uart.write(str(ldr1)+"\n")
   

```
using the serial is easy if screen is on linux

Find which device node the micro:bit was assigned to with the command ls /dev/ttyACM*.

If it was /dev/ttyACM0, type the command screen /dev/ttyACM0 115200

# maintenance

I needed to re flash the firmware to get micropython to work again

https://microbit.org/get-started/user-guide/firmware/

# May 4th Braitenberg vehicle

https://youtu.be/UafjlsHNAg4

The simple robot is a model of 
>Vehicle 2b
>The agent has the same two (left and right) symmetric sensors (e.g. light detectors), but each one stimulating a wheel on the other side of the body. It obeys the following rule:

>More light left → right wheel turns faster → turns towards the left, closer to the light.
>As a result, the robot follows the light; it moves to be closer to the light.

The LDRs are the sensors and are analog_read 0 -1023

The speed is analong_write 0-1023 

no mapping is necessary.

```Python
from microbit import *
ldr1 = 0
ldr2 = 0
uart.init(115200)
pin14.write_digital(1)

while True:
    
    display.off()
    
    ldr1 = pin0.read_analog() # read the ldrs
    ldr2 = pin3.read_analog()
    sleep(200)
    uart.write(str(ldr1)+ "   "+ str(ldr2)+"\n")
    pin1.write_analog(ldr1)  # speed control for a1 and a2
    pin13.write_digital(0)  # a1
    pin12.write_digital(1)  # a2

    pin2.write_analog(ldr2)  # speed control for b1 and b2

    pin15.write_digital(0)  # b 1
    pin16.write_digital(1)  # b2
        


```




# Whisker
 on Christmas day 2021 I finaly got my Whisker to work but there were problems
 
turtle3whisker.py
  this code works to simply move forward continuously until
  the whisker is triggered  then moves backwards and right around 180 degrees
  
  I killed a microbit (the blue one )  shorting out when hooking up the power
  
  really stupid mistake. 
  
  the motor controller seems to work but it doesn't send power to the microbit as it did before
  
  it now only sends power to the motors
  
  I have to hook up a separate 3v for the microbit to get it to work see video
  
  I will have to do this with an Arduino and try not to short that out
  
  
  https://youtu.be/jEU2HJGpL88
  

