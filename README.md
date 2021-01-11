# microbit
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

