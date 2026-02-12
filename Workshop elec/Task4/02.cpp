#include<Arduino.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

struct input{
  bool left,right,up,down;
};

int player_x = 30;
int player_y = 30;
const int speed = 4;

const unsigned int SCREEN_WIDTH = 128;
const unsigned int SCREEN_HEIGHT = 64;

const unsigned int DOWN = 7;
const unsigned int UP = 6;
const unsigned int LEFT = 5;
const unsigned int RIGHT = 4;

const unsigned long time_delay = 100;
unsigned long timer = 0;

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

input current_read;
input prev_read;
input inputs;


void draw(int x, int y, bool erase = false) {
  if (erase == false) {
    display.fillRect(x, y, 8, 8, SSD1306_WHITE); 
  }
  else if (erase == true){
    display.fillRect(x, y, 8, 8, SSD1306_BLACK); 
  }
  else{
    //just aise hi chumma
  }
  display.display();
  }

void update(input& inputs){
  if ( inputs.left == true ){
    if ( player_x - speed < 0){
      player_x = SCREEN_WIDTH - 8;
    }
    else{
      player_x = player_x - speed;
    }
  }
  if ( inputs.right == true ){
    if ( player_x + 8 + speed > SCREEN_WIDTH){
      player_x = 0;
    }
    else{
      player_x = player_x + speed;
    }
  }
  if ( inputs.down == true ){
    if ( player_y + 8 + speed > SCREEN_HEIGHT){
      player_y = 0;
    }
    else{
      player_y = player_y + speed;
    }
  }
  if ( inputs.up == true ){
    if ( player_y - speed < 0){
      player_y = SCREEN_HEIGHT - 8;
    }
    else{
      player_y = player_y - speed;
    }
  }
}
void setup(){
  pinMode(DOWN,INPUT_PULLUP);
  pinMode(UP,INPUT_PULLUP);
  pinMode(RIGHT,INPUT_PULLUP);
  pinMode(LEFT,INPUT_PULLUP);


    if((display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) == false) {
    Serial.println(F("SSD1306 allocation failed")); // Print error if init fails
    while(true); // Stay here forever if display is not detected
  }

  Serial.println("detected");
  display.clearDisplay(); 
  display.display();

  Serial.begin(9600);


  timer = millis();
}

void loop(){

  if ( millis() - timer > time_delay ){
    timer += time_delay;

    current_read.left = !digitalRead(LEFT);
    current_read.right = !digitalRead(RIGHT);
    current_read.down = !digitalRead(DOWN);
    current_read.up = !digitalRead(UP);

    inputs.left = current_read.left && !prev_read.left;
    inputs.right = current_read.right && !prev_read.right;
    inputs.up = current_read.up && !prev_read.up;
    inputs.down = current_read.down && !prev_read.down;

    draw(player_x,player_y,true);
    update(inputs);
    draw(player_x,player_y,false);


    Serial.print(" Left :");
    Serial.println(inputs.left);
    Serial.print(" right :");
    Serial.println(inputs.right);
    Serial.print(" up :");
    Serial.println(inputs.up);
    Serial.print(" down :");
    Serial.println(inputs.down);
    Serial.print("player pos : ");
    Serial.print(player_x);
    Serial.print( " - ");
    Serial.println(player_y);


    prev_read = current_read;

    
  }



}
