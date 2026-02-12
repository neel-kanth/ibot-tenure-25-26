#include<Arduino.h>
#include <Servo.h>

Servo servo_bbg;

int pos;

int servo_pin =3;


void setup(){
  servo_bbg.attach(servo_pin);
  
  pinMode(servo_pin,OUTPUT);
}

void loop(){
  pos = 180;
  // from 0 to 180
  //changed it in the video
  
  servo_bbg.write(pos);
}
