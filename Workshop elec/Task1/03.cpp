#include<Arduino.h>
const unsigned long time_delay = 100;
unsigned long prev_time = 0;

unsigned int state = 0;

unsigned int prev_buttonstate = 0;
unsigned int current_buttonstate = 0;

void setup(){
  pinMode(13,OUTPUT);
  pinMode(8,INPUT_PULLUP);
  Serial.begin(9600);
  prev_buttonstate = digitalRead(8);
}

void loop(){

  if (millis() - prev_time >= time_delay){
      prev_time = millis();
      current_buttonstate = digitalRead(8);
    if(prev_buttonstate == 1 && current_buttonstate == 0){
      state = !state;
    }
    prev_buttonstate = current_buttonstate;
    Serial.println(state);


    if(state == 1){
      digitalWrite(13,HIGH);
    }
    else if (state == 0){
      digitalWrite(13,LOW);
    }
  }
}