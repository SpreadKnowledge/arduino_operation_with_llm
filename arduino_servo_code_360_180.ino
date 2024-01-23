#include <Servo.h>

Servo servo360;  // 360度回るサーボモーター
Servo servo180;  // 180度回るサーボモーター

void setup() {
  servo360.attach(9);  // 360度サーボモーターをピン9に接続
  servo180.attach(10); // 180度サーボモーターをピン10に接続

  // サーボモーターを初期位置に設定
  servo360.write(0);
  servo180.write(90); // 180度サーボモーターの中心位置

  Serial.begin(9600);  // シリアル通信を9600ボーで開始
  Serial.println("Setup complete, Servos in initial position");
}

void loop() {
  if (Serial.available() > 0) {
    int angle360 = Serial.parseInt(); // 360度サーボモーターの角度を読み取る
    int duration180 = Serial.parseInt(); // 180度サーボモーターの動作時間を読み取る

    // 360度サーボモーターを動かす
    rotateServo360(angle360);
    delay(1000); // 動作後の待機時間

    // 180度サーボモーターを動かす
    moveServo180(duration180);
    delay(1000); // 動作後の待機時間

    // 360度サーボモーターを初期位置に戻す
    resetServo360();
  }
}

void rotateServo360(int angle) {
  servo360.write(angle); // 360度サーボモーターを指定の角度に回転させる
  Serial.print("Rotated 360 servo to: ");
  Serial.println(angle);
}

void moveServo180(int duration) {
  long endTime = millis() + duration * 1000; // 終了時間を計算
  while (millis() < endTime) {
    servo180.write(90);  // 中心から左に45度
    delay(500);
    servo180.write(135); // 中心から右に45度
    delay(500);
  }
  Serial.print("Moved 180 servo for: ");
  Serial.print(duration);
  Serial.println(" seconds");
}

void resetServo360() {
  servo360.write(0); // 360度サーボモーターを初期位置に戻す
  Serial.println("360 servo reset to initial position");
}