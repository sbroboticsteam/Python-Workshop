// globals pins and messages
const int directionPin = 7;
const int speedPin = 6;
const byte numChars = 3;
char msg[numChars];
boolean newData = false;
 
void setup()
{
  // initialize serial port and pins
  Serial.begin(9600);
  pinMode(directionPin, OUTPUT);
  pinMode(speedPin, OUTPUT);
}
 
void loop()
{
  recvWithEndMarker();
  showNewData();
}

// sets motor controller speed and direction
// 0 for forward, 1 for reverse
void setMotor(char speed, char reverse)
{
  if (speed == '0') {
    analogWrite(speedPin, 0);
  }
  analogWrite(speedPin, speed);
  boolean dir = LOW;
  if (reverse == 0) {
    dir = HIGH;
  } else if (reverse == 1) {
    dir = LOW;
  }
  digitalWrite(directionPin, dir);
}

// receive new messages over serial and put them in msg[]
void recvWithEndMarker() {
 static byte ndx = 0;
 char endMarker = '\n';
 char rc;
 
 // if (Serial.available() > 0) {
 while (Serial.available() > 0 && newData == false) {
  rc = Serial.read();

  if (rc != endMarker) {
   msg[ndx] = rc;
   ndx++;
   if (ndx >= numChars) {
    ndx = numChars - 1;
   }
  } else {
   msg[ndx] = '\0'; // terminate the string
   ndx = 0;
   newData = true;
  }
 }
}

// help us debug by showing us the data we got and then call setMotor()
void showNewData() {
 if (newData == true) {
 //Serial.print("This just in ... ");
 //Serial.println(msg);
 setMotor(msg[0], msg[1]);
 newData = false;
 }
}
    
  
