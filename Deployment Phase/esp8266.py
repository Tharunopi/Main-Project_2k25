import serial
import time

esp = serial.Serial("COM24", 115200, timeout=1)  # Change COM24 to your port
time.sleep(2)  # Wait for connection

while True:
    angle1 = input("Enter angle for Servo 1 (0-180) or 'exit' to quit: ")
    if angle1.lower() == 'exit':
        break

    angle2 = input("Enter angle for Servo 2 (0-180): ")

    try:
        angle1 = int(angle1)
        angle2 = int(angle2)
        if 0 <= angle1 <= 180 and 0 <= angle2 <= 180:
            command = f"{angle1} {angle2}\n"
            esp.write(command.encode())  # Send angles to ESP8266
            time.sleep(0.5)  # Wait for ESP response
            response = esp.readline().decode(errors='ignore').strip()
            print("ESP Response:", response)
        else:
            print("Angles must be between 0 and 180!")
    except ValueError:
        print("Please enter valid numbers!")

esp.close()
