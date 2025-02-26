import time, serial

esp = serial.Serial("COM24", 9600, timeout=1)
time.sleep(2)  # Wait 3 seconds for ESP to initialize
esp.flush()

positions = [
    # (0, 0),   # Top-left
    # (180, 0),  # Top-right
    # (0, 180),  # Bottom-left
    # (180, 180),# Bottom-right
    (90, 90)   # Center
]
for i in positions:
    ang1, ang2 = i
    command = f"{ang1} {ang2}\n"
    esp.write(command.encode())
    time.sleep(0.5)
    response = esp.readline().decode(errors='ignore').strip()
    print("ESP Response:", response)

esp.close()