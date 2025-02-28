import serial
import time


# Configure the serial connection
def setup_serial_connection(port, baud_rate=9600):
    try:
        ser = serial.Serial(port, baud_rate, timeout=1)
        time.sleep(2)  # Allow time for connection to establish
        ser.flushInput()  # Clear any initial garbage data
        return ser
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        return None


def main():
    # Update the port based on your system
    port = 'COM24'  # Change this to match your port

    ser = setup_serial_connection(port)
    if not ser:
        print("Failed to connect to ESP8266")
        return

    print("Starting distance monitoring...")
    try:
        while True:
            if ser.in_waiting > 0:
                try:
                    line = ser.readline().decode('utf-8', errors='replace').strip()
                    try:
                        distance = float(line)
                        print(f"Distance: {distance:.2f} cm")
                    except ValueError:
                        # Only print if there's actual content
                        if line:
                            print(f"Received non-numeric data: {line}")
                except Exception as e:
                    print(f"Error reading from serial: {e}")
                    ser.flushInput()  # Clear buffer on error
            time.sleep(0.5)  # Small delay to prevent CPU hogging
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user")
    finally:
        ser.close()
        print("Serial connection closed")


if __name__ == "__main__":
    main()