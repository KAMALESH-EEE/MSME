from machine import UART
import time



com = UART(0, baudrate = 115200)
while True:
    com.write('HAI from HOST')
    print(com.read())
    time.sleep(1)