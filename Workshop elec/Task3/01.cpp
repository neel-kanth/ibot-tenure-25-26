#include<Arduino.h>

void setup(){

}

void loop(){
    Tone(4,1000);
    delay(1000);
    noTone(4);
    delay(1000);
}
