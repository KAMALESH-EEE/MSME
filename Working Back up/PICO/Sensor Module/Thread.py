# from machine import Pin, UART
# from dht11 import read_DHT, InvalidChecksum
# import time,utime
# 
# gps = UART(0,baudrate=9600)
# dht_pin = Pin(4)
# 
# trigger = Pin(18, Pin.OUT)
# echo = Pin(19, Pin.IN)
# 
# 
# def read_gps_data():
#     gps.read()
#     time.sleep(1)
#     i=0
#     while True:
#         i+=1
#         if gps.any():
#             gps_data = str(gps.readline())
#             #print(gps_data)
#             if('$GPGGA' in gps_data):
#                 parts = gps_data.split(',')
#                 #print(parts)
#                 if len(parts) >= 10 and parts[2] != b'' and parts[4] != b'':
#                     latitude = float(parts[2][0:2]) + float(parts[2][2:]) / 60.0
#                     if parts[3] == b'S':
#                         latitude = -latitude
#                     longitude = float(parts[4][0:3]) + float(parts[4][3:]) / 60.0
#                     if parts[5] == b'W': 
#                         longitude = -longitude
#                     return latitude, longitude
#         if i==10:
#             print('GPS timeout')
#             return None
# def read_gps_time():
#     gps.read()
#     time.sleep(1)
#     i=0
#     while True:
#         i+=1
#         if gps.any():
#             line = str(gps.readline())
#             #print(line)
#             if ('$GNGGA'in line) or ('$GPGGA' in line):
#                 parts = line.split(',')
#             
#                 if len(parts) >= 2:
#                     p = parts[1]
#                     h=int(p[0:2])
#                     m=int(p[2:4])
#                     s=int(float(p[4::])+3)
#                     m+=(30+int(s/60))
#                     s%=60
#                     h+=int(m/60)
#                     m%=60
#                     h+=5
#                     h%=24
#                     return f'{h}:{m}:{s}'                    
#         if i ==10:
#             print('RTC timeout')
#             return None
#         
# def distance():
#     trigger.low()
#     utime.sleep_us(2)
#     trigger.high()
#     utime.sleep_us(5)
#     trigger.low()
#     while echo.value() == 0:
#         signaloff = utime.ticks_us()
#     while echo.value() == 1:
#        signalon = utime.ticks_us()
#     timepassed = signalon - signaloff
#     distance = (timepassed * 0.0343) / 2
#     return distance
#     
#         
# sen=[read_DHT,distance,read_gps_data,read_gps_time]
# 
# while True:
#     for i in sen:
#         print(i())
#     
#

from SM import distance
import time


while True:
    print(distance())
    time.sleep(1)