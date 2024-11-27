from machine import Pin, UART
from dht11 import read_DHT, InvalidChecksum
import time,utime

gps = UART(1,tx=Pin(4),rx=Pin(5),baudrate=9600)
dht_pin = Pin(4)

led = Pin(25,Pin.OUT)

trigger_pin = Pin(18, Pin.OUT)
echo_pin = Pin(19, Pin.IN)

SP = Pin(10,Pin.OUT)
SP.off()

tf=True

def read_gps_data():
    i=0
    while True:
        i+=1
        time.sleep(0.1)
        if gps.any():
            
            gps_data = str(gps.readline())
            #print(gps_data)
            if('$GPGGA' in gps_data):
                parts = gps_data.split(',')
                #print(parts)
                if len(parts) >= 10 and parts[2] != b'' and parts[4] != b'':
                    latitude = float(parts[2][0:2]) + float(parts[2][2:]) / 60.0
                    if parts[3] == b'S':
                        latitude = -latitude
                    longitude = float(parts[4][0:3]) + float(parts[4][3:]) / 60.0
                    if parts[5] == b'W': 
                        longitude = -longitude
                    return latitude, longitude
        if i==20:
            print('GPS timeout')
            return None
def read_gps_time():
    try:
        i=0
        while True:
            time.sleep(0.1)
            i+=1
            if gps.any():
                line = str(gps.readline())
                #print(line)
                if ('$GNGGA'in line) or ('$GPGGA' in line):
                    parts = line.split(',')
                
                    if len(parts) >= 2:
                        p = parts[1]
                        h=int(p[0:2])
                        m=int(p[2:4])
                        s=int(float(p[4::])+3)
                        m+=(30+int(s/60))
                        s%=60
                        h+=int(m/60)
                        m%=60
                        h+=5
                        h%=24
                        return f'{h}:{m}:{s}'                    
            if i ==20:
                print('RTC timeout')
                return None
    except :
        led.on()
        print('error @ SM_RTC')
        return None
        
def distance():
    trigger_pin.value(0)
    utime.sleep_us(2)
    trigger_pin.value(1)
    utime.sleep_us(10)
    trigger_pin.value(0)

    start_time = utime.ticks_ms()
    while echo_pin.value() == 0:
        if utime.ticks_diff(utime.ticks_ms(), start_time) > 5000:
            return None
    pulse_start = utime.ticks_us()
    
    start_time = utime.ticks_ms()
    while echo_pin.value() == 1:
        if utime.ticks_diff(utime.ticks_ms(), start_time) > 5000:
            return None
    pulse_end = utime.ticks_us()
    pulse_duration = utime.ticks_diff(pulse_end, pulse_start)
    
    distance_cm = pulse_duration / 58
    
    return distance_cm
    
def Spray():
    SP.on()
    time.sleep(2)
    SP.off()
    return 1
        
sen=[read_DHT,distance,read_gps_data,read_gps_time,Spray]
 
