// ESP8266 with distance sensor (HC-SR04) using D8 and D7
const int trigPin = D8;  // D8 is GPIO15 on ESP8266
const int echoPin = D7;  // D7 is GPIO13 on ESP8266

void setup() {
  // Initialize Serial connection
  Serial.begin(115200);

  // Initialize pins
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  Serial.println("Distance Sensor Ready");
}

float measureDistance() {
  // Clear the trigger pin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  // Set the trigger pin HIGH for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Read the echo pin, returns the sound wave travel time in microseconds
  long duration = pulseIn(echoPin, HIGH);

  // Calculate the distance
  float distance = duration * 0.034 / 2;

  return distance;
}

void loop() {
  // Measure distance
  float distance = measureDistance();

  // Send distance over serial
  Serial.println(distance);

  delay(100); // Measure 10 times per second
}