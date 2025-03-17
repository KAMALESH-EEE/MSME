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



#========= HOST decleration ==============

HOST = DEV(0,'HOST')

DATA[0] = 'Driving System'
DATA[1] = 2

LED = Pin(25,Pin.OUT)
LED.off()



#==== PINs for Motors =======

FLF = PWM(Pin(18), freq=100)
FLB = PWM(Pin(19), freq=100)
FRF = PWM(Pin(15), freq=100)
FRB = PWM(Pin(14), freq=100)

RLF = PWM(Pin(20), freq=100)
RLB = PWM(Pin(21), freq=100)
RRF = PWM(Pin(13), freq=100)
RRB = PWM(Pin(12), freq=100)


#======== PWM PINs for Servo ========

FLD = PWM(Pin(17), freq=50)
FRD = PWM(Pin(16), freq=50)
RLD = PWM(Pin(7), freq=50)
RRD = PWM(Pin(8), freq=50)


#======== Servo Control Function ========

def servo(angle):
    angle = angle + 90
    if angle>=0 and angle<=180:
        return int(1900+(angle/180)*6100)
    return servo(90) # Streeing Disabled 


#======== Grouping PINs =========

fmotors = [FLF,RLF,FRF,RRF]
rmotors = [FLB,RLB,FRB,RRB]
Lmotors = [FLF,FLB,RLF,RLB]
Rmotors = [FRF,FRB,RRF,RRB]

FSD = [FLD,FRD]
RSD = [RLD,RRD]


#======== Basic Functions =========

'''
    Registers Details:
    0 to 4 :Reserved
    5:Moving Operation {0:stop , 1:forward, 2: Reversed, 3:turn Right, 4:turn Left}
    6:Speed
    7:Input angle
    8:Servo Last set angle
      
'''

def forward(s):
    print(f'forward [{s}]')
    for m in rmotors:
        m.duty_u16(0)
    for m in fmotors:
        m.duty_u16(s)
    
def reverse(s):
    print(f'reverse [{s}]')
    for m in fmotors:
        m.duty_u16(0)
    for m in rmotors:
        m.duty_u16(s)

def stop(s=0):
    print(f'stop [{s}]')
    for m in rmotors:
        m.duty_u16(0)
    for m in fmotors:
        m.duty_u16(0)

#======== Steering Defination============

def Steering(Sers):
    forward(int(DATA[6]/4))
    while not(DATA[8]==DATA[7]):
        if DATA[8]>DATA[7]:
            DATA[8]-=1
        elif DATA[8]<DATA[7]:
            DATA[8]+=1
        else:
            print("No Changes")

        for i in Sers:
            i.duty_u16(servo(DATA[8]))
        print(Sers,"Set"+DATA[8])
        
        if HOST.Receive():
            stop()
            break
        
        utime.sleep(0.05)
    stop()

    



#++++++++++++++++++++++++++++++++++++

CMD =[stop,forward,reverse,Steering]



