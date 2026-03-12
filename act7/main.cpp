#include <Arduino.h>
#include <Servo.h>

Servo myServo;
const int servoPin = 9;

void setup() {
  Serial.begin(9600);

  myServo.attach(servoPin);
  myServo.write(90);

  Serial.println("Arduino Ready!");
}

void loop() {

  if (Serial.available() > 0) {

    String received = Serial.readStringUntil('\n');
    received.trim();

    if (received.length() == 0) return;

    long angle = received.toInt();

    if (angle == 0 && received != "0") {
      Serial.println("Error: Numbers only!");
    }

    else if (angle < 0 || angle > 180) {
      Serial.println("Error: Angle must be 0-180!");
    }

    else {
      myServo.write(angle);
      Serial.print("Moved to: ");
      Serial.println(angle);
    }
  }
}