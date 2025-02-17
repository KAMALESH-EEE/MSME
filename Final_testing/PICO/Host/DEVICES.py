'''
File    : DEVICES.py
Author  : Kamalesh R
Version : 0V02
created : 04/02/2025
Device  : HOST

This file only for HOST module which includes the other module property declearation and BITE

'''

from LIB import *
from machine import Pin
import utime

#============= Declearing Modules ======================

print("Device Declearing ....")
_DD = DEV(1,"Disease Detector",True)
_DS = DEV(2,"Driving System",True)
_SM = DEV(3,"Sensor Module",True)
HC = UART(1, tx =Pin(4),rx = Pin(5), baudrate=9600)

led = Pin(25,Pin.OUT)

D1 = Pin(6,Pin.OUT) #Main Loop
D2 = Pin(7,Pin.OUT) #Waiting for User Input
D3 = Pin(8,Pin.OUT) #Waiting for Module Response
D4 = Pin(9,Pin.OUT) #Error

MyDevices = [_DD,_DS,_SM]
print("All Devices are Decleared \n PBIT:")
led.on()



#================ HC operation ===================

def Input(s):
    HC.write(s+'\n')
    while not (HC.any()):
        pass
    t=str(HC.read()).split("'")
    return t[1]

def Print(s):
    print(s)
    HC.write(s+'\n')


#================= PBITE =========================
PBIT=True
for dev in MyDevices:
    dev.BITE()
    print(f"{dev.Name} : {dev.BITE_Status}")
    PBIT = PBIT and dev.BITE_Status

Print(f"PBIT result {"PASS" if PBIT else "FAIL"}")
led.off()


#================ DS operation ===================

class DS:

    '''
    Registers Details:
    1 to 4 :Reserved
    5:Moving Operation {0:stop , 1:forward, 2: Reversed, 3:turn Right, 4:turn Left}
    6:Speed
      
    '''
    ListSpeed=[6553, 13106, 19659, 26212, 32765, 39318, 45871, 52424, 58977, 65534]
    
    def stop():
        _DS.Write(5,0)
    
    def forward():
        _DS.Write(5,1)

    def backward():
        _DS.Write(5,2)
    
    def right():
        _DS.Write(5,3)
    
    def left():
        _DS.Write(5,4)


    def set_speed(a):
        if (a>=0 and a<10):
            _DS.Write(6,a)
            if a == 9:
                Print
        else:
            Print("Speed out of Range")
        
    def speed_up():
        a=_DS.Read(6)
        DS.set_speed(a+1)

    def speed_down():
        a=_DS.Read(6)
        DS.set_speed(a-1)