/* need to check the string comming in by
looking at the first character.  like c " " is for a string
and ' ' is for character so pay attention when checking
changes



*/


import processing.serial.*;

float x, y;

Serial myPort;  // Create object from Serial class
String val;      // Data received from the serial port
String oldVal = "N";
String newVal;
void setup() 
{
  size(400, 400);
   
  String portName = Serial.list()[0];
  myPort = new Serial(this, portName, 115200);
  myPort.bufferUntil(10);
  x= width/2;
  y=height/2;
}


void draw() {
  
 background(0);
 if ( myPort.available() > 0) {  // If data is available,
    val = myPort.readString();         // read it and store it in val
    
    val = trim(val);
    println(val);
 
    if (val.charAt(0) == 'L'){
     x=x-10;
     println("bing");
   }
   else if(val.charAt(0) == 'R'){
     
     x=x+10;
   
   
 }
    
 }
 
  
  stroke(255);
 fill(127);
 ellipse(x,y,20,20);

}
