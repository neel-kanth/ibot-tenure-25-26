#include<Arduino.h>


int TRIG = 3;           // Trigger pin of HC-SR04
int ECHO = 2;           // Echo pin of HC-SR04
float distance_cm = 0;
float time_diff_us;  // Pulse travel time (µs)

int distance_average;
const float alpha = 0.1;
void setup(){  
  pinMode(TRIG,OUTPUT);       // Set trigger as output
  pinMode(ECHO,INPUT);        // Set echo as input
  
  Serial.begin(9600);         // Start serial monitor
}

void loop(){
  // Send ultrasonic trigger pulse for 10 microseconds
  digitalWrite(TRIG,LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG,HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG,LOW);
  
  
  
  // Measure echo pulse duration
  time_diff_us = pulseIn(ECHO, HIGH, 30000);
  // NOTE THAT pulseIn is a blocking function.
  
  // Convert to distance in cm (speed of sound = 0.0343 cm/µs)
  distance_cm = 0.343*time_diff_us/20;
  
  Serial.println(distance_cm);

  
}

//time_diff_us was not returning 0, if object wasnt found. it was
//just giving the maximum value, hence i did distance_cm>334.0
// for object not found case.


//Theres a resistor attached to the wire attached to ECHO, because 
// it was mentioned to do so in the datahsheet of HC-SR04, as it outputs 5v and may damage the pins.


//am getting constant +-1cm error in the reading,  i think that some
//extra-few lines also being run will casue some microsecond delay
//which will cause a +-1cm error.
//just a thought, nothing conclusive
