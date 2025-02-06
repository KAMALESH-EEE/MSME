'''
File    : DEVICES.py
Author  : Kamalesh R
Version : 0V02
created : 04/02/2025
Device  : HOST

This file only for HOST module which includes the other module property declearation and BITE

'''

from dev import *
from machine import Pin
import utime

#============= Declearing Modules ======================

print("Device Declearing ....")
_DD = DEV(1,"Disease Detector",True)
_DS = DEV(2,"Driving System",True)
_SM = DEV(3,"Sensor Module",True)

MyDevices = [_DD,_DS,_SM]
print("All Devices are Decleared \n PBIT:")


#================= PBITE =========================
PBIT=True
for dev in MyDevices:
    dev.BITE()
    print(f"{dev.Name} {dev.BITE}")
    PBITE = PBITE and dev.BITE

print(f"PBIT result {"PASS" if PBITE else "FAIL"}")

#================ DS operation ===================

class DS:

    '''
    Registers Details:
    1 to 4 :Reserved
    5:Moving Operation {0:stop , 1:forward, 2: Reversed, 3:turn Right, 4:turn Left}
    6:Speed
      
    '''
    
    def stop():
        _DS.Write(5,0)
    





