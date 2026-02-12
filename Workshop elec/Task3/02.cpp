#include<Arduino.h>
#include <LiquidCrystal.h>

const int rw = 12;
const int rs = 13;
const int en = 11;
const int d4 = 10;
const int d5 = 9;
const int d6 = 8;
const int d7 = 7;

LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
  pinMode(rw,OUTPUT);
  digitalWrite(rw,LOW);

  Serial.begin(9600);

  lcd.begin(16, 2);

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("hello peeps");
}

void loop() {

}