'''
File    : DEVICES.py
Author  : Kamalesh R
Version : 0V02
created : 04/02/2025
Device  : Driving System

This file only for Driving System which includes the IO mapping and its Functions.

'''

from dev import *
from machine import Pin, PWM
import utime

from dht11 import read_DHT, InvalidChecksum
from HC_SR04 import HCSR04



#========= HOST decleration ==============

HOST = DEV(0,'HOST')

DATA[0] = 'Sensor Module'
DATA[1] = 3

LED = Pin(25,Pin.OUT)
LED.off()



#==== PINs for Sprayer Driver =======

Sprayer = PWM(Pin(18), freq=100)

#==== Ultrasonic Sensor =============

TriPin = None
EchoPin = None

US = HCSR04(TriPin, EchoPin)


#======== Basic Functions =========
'''
    Registers Details:
    1 to 4 :Reserved
    5:DHT-Temp
    6:DHT-Hum
    7:Distance
    8:GPS-LAT
    9:GPS-LON
    10:Soil Mosture
    11:
    15:Functional Block{S:Spray Fertlizer}
    
'''

#==== DTH Function Definition ================

def Read_DHT():
    Temp, Hum = read_DHT()
    DATA[5] = Temp
    DATA[6] = Hum

#==== Distance Function Definition ===========
def Distance():
    pass


#==== Sprayer Function Definition =============

def Spray():
    if not ( 'S' in DATA[15]):
        return
    Sprayer.duty_u16(DATA[16])
    DATA[15] = 0
    utime.sleep(DATA[17])
    Sprayer.duty_u16(0)

#++++++++++++++++++++++++++++++++++++

CMD =[Read_DHT, Distance, HOST.Receive, Spray]



