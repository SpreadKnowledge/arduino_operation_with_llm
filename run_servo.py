import serial
import time

arduino = serial.Serial('COM4', 9600, timeout=1)
time.sleep(2)  # Arduinoのリセット待ち

def send_command(angle360, duration):
    command = f"{angle360} {duration}\n"
    arduino.write(command.encode())

# 例: 360度サーボを180度に回転させ、180度サーボを5秒間動かす
degree = 180

send_command(degree, 6)