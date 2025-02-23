#include <Servo.h>

Servo servoX;  // left-right servo
Servo servoY;  // up-down servo

const int SERVO_X_PIN = D1;  // left-right servo pin
const int SERVO_Y_PIN = D2;  // up-down servo pin

void setup() {
  Serial.begin(9600);

  servoX.attach(SERVO_X_PIN);
  servoY.attach(SERVO_Y_PIN);

  // Initialize servos to center position
  servoX.write(90);
  servoY.write(90);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');

    // Split the received string into x and y values
    int commaIndex = data.indexOf(',');
    if (commaIndex != -1) {
      int x = data.substring(0, commaIndex).toInt();
      int y = data.substring(commaIndex + 1).toInt();

      // Move servos to the desired positions
      servoX.write(x);
      servoY.write(y);
    }
  }
}