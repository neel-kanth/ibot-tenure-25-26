#include<Arduino.h>
const unsigned int sensor_pin = A0;
int sensor_read = 0;
const unsigned int led_pin = 13;

void setup(){
  pinMode(sensor_pin,INPUT);
  pinMode(led_pin,OUTPUT);
  Serial.begin(9600);
}

void loop(){
  sensor_read = analogRead(sensor_pin);

  if(sensor_read > 700){
    digitalWrite(led_pin,HIGH);
    delay(1000);
    digitalWrite(led_pin,LOW);
  }
  Serial.println(sensor_read);
  delay(100);
}