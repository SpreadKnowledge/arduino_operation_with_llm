#include <Servo.h>

Servo servo1;  // 最初のサーボモーター
Servo servo2;  // 2番目のサーボモーター
bool isCommandReceived = false;

void setup() {
  servo1.attach(9);  // 最初のサーボモーターをピン9に接続
  servo2.attach(10); // 2番目のサーボモーターをピン10に接続
  servo1.write(90);  // 初期位置に設定
  servo2.write(90);  // 初期位置に設定
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0 && !isCommandReceived) {
    int angle = Serial.parseInt();
    int duration = Serial.parseInt();

    if (angle >= 0 && angle <= 180) {
      servo1.write(angle);  // 角度を設定
      delay(1000);

      long endTime = millis() + duration * 1000;
      while (millis() < endTime) {
        servo2.write(75);
        delay(250);
        servo2.write(105);
        delay(250);
      }

      servo1.write(90);  // 初期位置に戻す
      delay(1000);
      isCommandReceived = true;
    }
  }
}