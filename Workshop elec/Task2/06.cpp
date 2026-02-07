#include<Arduino.h>
const unsigned int sensor_pin = A0;
int sensor_read = 0;

void setup(){
  pinMode(sensor_pin,INPUT);
  Serial.begin(9600);
}

void loop(){
  sensor_read = analogRead(sensor_pin);
  Serial.println(sensor_read);
  delay(100);
}
