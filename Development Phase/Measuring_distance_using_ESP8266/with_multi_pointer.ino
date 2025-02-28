#include <Servo.h>

// Servo pins
const int SERVO_X_PIN = D1;  // left-right servo
const int SERVO_Y_PIN = D2;  // up-down servo

// Ultrasonic sensor pins
const int trigPin = D8;  // Trigger pin connected to D8 (GPIO15)
const int echoPin = D7;  // Echo pin connected to D7 (GPIO13)

// Create servo objects
Servo servoX;
Servo servoY;

// For smoothing servo movement
int currentX = 90;
int currentY = 90;
int targetX = 90;
int targetY = 90;
const int smoothingFactor = 5;  // Higher value = slower, smoother movement

// Timing variables
unsigned long lastDistanceMeasurement = 0;
const int distanceInterval = 100;  // Measure distance every 100ms

void setup() {
  // Initialize serial communication
  Serial.begin(9600);

  // Configure servo pins
  servoX.attach(SERVO_X_PIN);
  servoY.attach(SERVO_Y_PIN);

  // Initialize servos to center position
  servoX.write(90);
  servoY.write(90);

  // Configure ultrasonic sensor pins
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  digitalWrite(trigPin, LOW);

  delay(1000);  // Give servos time to reach initial position
  Serial.println("ESP8266 Servo and Distance Sensor Ready");
}

void loop() {
  // 1. Check for servo control commands
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');

    // Check if this is a distance request or servo command
    if (data == "DISTANCE") {
      // Send distance measurement
      float distance = measureDistance();
      Serial.println(distance);
    }
    else {
      // Parse the data for servo X and Y coordinates
      int commaIndex = data.indexOf(',');
      if (commaIndex != -1) {
        // Extract values
        targetX = data.substring(0, commaIndex).toInt();
        targetY = data.substring(commaIndex + 1).toInt();

        // Constrain values to valid servo range
        targetX = constrain(targetX, 0, 180);
        targetY = constrain(targetY, 0, 180);
      }
    }
  }

  // 2. Periodically measure and send distance
  unsigned long currentMillis = millis();
  if (currentMillis - lastDistanceMeasurement >= distanceInterval) {
    lastDistanceMeasurement = currentMillis;
    float distance = measureDistance();

    // Only send valid readings (to avoid flooding the serial)
    if (distance > 0 && distance < 400) {
      Serial.print("DIST:");  // Add a prefix to identify distance readings
      Serial.println(distance);
    }
  }

  // 3. Update servo positions with smoothing
  if (currentX != targetX || currentY != targetY) {
    // Update X position with smoothing
    if (currentX < targetX) {
      currentX = min(currentX + smoothingFactor, targetX);
    } else if (currentX > targetX) {
      currentX = max(currentX - smoothingFactor, targetX);
    }

    // Update Y position with smoothing
    if (currentY < targetY) {
      currentY = min(currentY + smoothingFactor, targetY);
    } else if (currentY > targetY) {
      currentY = max(currentY - smoothingFactor, targetY);
    }

    // Move servos to new positions
    servoX.write(currentX);
    servoY.write(currentY);

    // Short delay for smoother motion
    delay(15);
  } else {
    // If no movement needed, short delay to prevent CPU hogging
    delay(10);
  }
}

float measureDistance() {
  // Clear the trigger pin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  // Send a 10μs pulse to trigger
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Read duration of echo pulse (in microseconds)
  long duration = pulseIn(echoPin, HIGH, 30000);  // 30ms timeout

  // Calculate distance in centimeters
  float distance = duration * 0.0343 / 2;

  return distance;
}