# Python code to control 1 motor
import time, serial

esp = serial.Serial("COM24", 9600, timeout=1)
time.sleep(2)  # Wait 2 seconds for Arduino to initialize
esp.flush()

positions = [0, 45, 90, 135, 180, 90, 0]  # Different angles for the motor

for angle in positions:
    command = f"{angle}\n"
    esp.write(command.encode())
    time.sleep(0.5)
    response = esp.readline().decode(errors='ignore').strip()
    print("Arduino Response:", response)

esp.close()