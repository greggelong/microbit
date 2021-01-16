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



