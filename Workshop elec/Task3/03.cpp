#include<Arduino.h>

#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

const unsigned int SCREEN_WIDTH = 128;
const unsigned int SCREEN_HEIGHT = 64;

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

void setup(){
  Serial.begin(9600);

  // Initialize the SSD1306 display at I2C address 0x3C
  if((display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) == false) {
    Serial.println(F("SSD1306 allocation failed")); // Print error if init fails
    while(true); // Stay here forever if display is not detected
  }

  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0,0);
  display.println("Svk anna why?");
  display.display();

}

void loop(){

  Serial.println("hi)");

}