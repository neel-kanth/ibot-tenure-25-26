#include<Arduino.h>
int brightness = -1;
int increment = 1;

void setup(){
  pinMode(13,INPUT);
  pinMode(13,OUTPUT);
  Serial.begin(9600);
}

void loop(){
  if(brightness >= 255){
    increment = -1;
  }
  else if(brightness <=0){
    increment = + 1;
  }

  brightness += increment;
  analogWrite(11,brightness);
  Serial.println(brightness);
}
