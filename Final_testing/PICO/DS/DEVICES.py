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
    if angle>=0 and angle<=180:
        return int(1900+(angle/180)*6100)
    return servo(90) # Streeing Disabled 


#======== Grouping PINs =========

fmotors = [FLF,RLF,FRF,RRF]
rmotors = [FLB,RLB,FRB,RRB]
Lmotors = [FLF,FLB,RLF,RLB]
Rmotors = [FRF,FRB,RRF,RRB]


#======== Basic Functions =========

'''
    Registers Details:
    1 to 4 :Reserved
    5:Moving Operation {0:stop , 1:forward, 2: Reversed, 3:turn Right, 4:turn Left}
    6:Speed
      
'''

def forward(s):
    for m in rmotors:
        m.duty_u16(0)
    for m in fmotors:
        m.duty_u16(s)
    
def reverse(s):
    for m in fmotors:
        m.duty_u16(0)
    for m in rmotors:
        m.duty_u16(s)

def stop(s):
    for m in rmotors:
        m.duty_u16(0)
    for m in fmotors:
        m.duty_u16(0)

#++++++++++++++++++++++++++++++++++++

