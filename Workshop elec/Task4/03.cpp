#incldue <Arduino.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

const int unsigned sensor_pin = A0;
int sensor_read = 0;
int old_sensor_read = 32;

const unsigned int SCREEN_WIDTH = 128;
const unsigned int SCREEN_HEIGHT = 64;


Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

void draw_bar(int value, uint16_t color) {
  int h = abs(value);            
  int y_start;

  if (value < 0) {
    y_start = 32 - h;         
  } else {
    y_start = 32;                 
  }

  display.fillRect(64, y_start, 20, h, color);
}

void setup(){

  pinMode(sensor_pin,INPUT);
  pinMode(9,OUTPUT);
  digitalWrite(9,HIGH);
  Serial.begin(9600);


    if((display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) == false) {
    Serial.println(F("SSD1306 allocation failed")); // Print error if init fails
    while(true); // Stay here forever if display is not detected
  }

  Serial.println("detected");
  display.clearDisplay(); 
  display.display();

}
void loop(){ 
  
  draw_bar(old_sensor_read,SSD1306_BLACK);
  sensor_read = map(analogRead(sensor_pin),0,1024,-30,30);
  Serial.println(sensor_read);

  if(sensor_read == 0){
    sensor_read = 1;
  }

  draw_bar(sensor_read,SSD1306_WHITE);

  display.display();

  old_sensor_read = sensor_read;

  delay(10);

}