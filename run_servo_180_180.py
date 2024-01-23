import serial
import time

degree_table = 0
shake_time = 6

arduino = serial.Serial('COM4', 9600, timeout=1)
time.sleep(2)  # Arduinoのリセット待ち

def send_command(angle, duration):
    command = f"{angle} {duration}\n"
    arduino.write(command.encode())

# 例: 最初のサーボモーターを90度に回転させ、2つ目のサーボモーターを10秒間45度左右に動かす
send_command(degree_table, shake_time)