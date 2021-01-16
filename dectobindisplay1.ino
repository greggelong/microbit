// https://forum.arduino.cc/index.php?topic=333006.0
int dt = 1000;
int ones = 10;
int twos = 11;
int fours = 12;
int eights = 13;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(ones,OUTPUT);
  pinMode(twos,OUTPUT);
  pinMode(fours,OUTPUT);
  pinMode(eights,OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
 
   for(int i = 0; i <16; i++){
   Serial.println(i);
   int n = i;
   uint8_t bitsCount = sizeof( n ) * 8;
   char binstr[ bitsCount + 1 ];
   uint8_t j = 0;
   while ( bitsCount-- ){
      binstr[ j++ ] = bitRead( n, bitsCount ) + '0';
      binstr[ j ] = '\0';

   }
   Serial.println( binstr );
   Serial.println(binstr[15]);
   // ones
   if(binstr[15] == '1'){
    Serial.println("high");
    digitalWrite(ones,HIGH);
   }
   else{
    Serial.println("low");
    digitalWrite(ones,LOW);
   }
   // twos
   if(binstr[14] == '1'){
    Serial.println("high");
    digitalWrite(twos,HIGH);
   }
   else{
    Serial.println("low");
    digitalWrite(twos,LOW);
   }
   // fours
   if(binstr[13] == '1'){
    Serial.println("high");
    digitalWrite(fours,HIGH);
   }
   else{
    Serial.println("low");
    digitalWrite(fours,LOW);
   }
   // eights
   if(binstr[12] == '1'){
    Serial.println("high");
    digitalWrite(eights,HIGH);
   }
   else{
    Serial.println("low");
    digitalWrite(eights,LOW);
   }
   
   delay(dt);
   digitalWrite(ones,LOW);
   digitalWrite(twos,LOW);
   digitalWrite(fours,LOW);
   digitalWrite(eights,LOW);
   delay(dt);
  
   }
}
