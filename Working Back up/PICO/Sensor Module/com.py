from machine import Pin,UART
import time

HC = UART(1,tx = Pin(4),rx = Pin(5),baudrate =9600)

print(HC)

HC.write('Hello\n')
