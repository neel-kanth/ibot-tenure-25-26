#include<Arduino.h>
const unsigned int pin_read = A5;
int pin_value;
int pin_value_average;
const float alpha = 0.25;

void setup() {
  pinMode(pin_read,INPUT);
  Serial.begin(9600);
}

void loop(){
  pin_value = analogRead(pin_read);
  
  pin_value_average = pin_value_average + alpha * ( pin_value - pin_value_average );
  Serial.println(pin_value_average);
  delay(50);
}
