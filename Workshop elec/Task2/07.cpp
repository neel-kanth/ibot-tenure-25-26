#include<Arduino.h>
#include <DHT.h>
const unsigned int sensor_pin = 7;
float humidity;
float temperature;

DHT dht(sensor_pin, DHT11);

void setup(){
  Serial.begin(9600);
  dht.begin();
}

void loop(){
  humidity = dht.readHumidity();
  temperature = dht.readTemperature();

  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.print(" %   ");

  Serial.print("Temp: ");
  Serial.print(temperature);
  Serial.println("C");

  delay(2000);
}