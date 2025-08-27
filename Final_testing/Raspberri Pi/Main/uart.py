import serial

# Open UART on /dev/serial0 at 115200 baud
ser = serial.Serial("/dev/serial0", baudrate=115200, timeout=1)

ser.write(b"Hello from Raspberry Pi!\n")

while True:
    if ser.in_waiting > 0:
        data = ser.readline().decode('utf-8').strip()
        print("Received:", data)