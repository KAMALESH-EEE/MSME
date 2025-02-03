from machine import Pin,PWM
import utime

max_Speed = (2**16)-1
Speed=5

spm = Pin(4,Pin.OUT)
spm.off()

FLF = PWM(Pin(18), freq=100)
FLB = PWM(Pin(19), freq=100)
FRF = PWM(Pin(15), freq=100)
FRB = PWM(Pin(14), freq=100)


RLF = PWM(Pin(20), freq=100)
RLB = PWM(Pin(21), freq=100)
RRF = PWM(Pin(13), freq=100)
RRB = PWM(Pin(12), freq=100)


FLD = PWM(Pin(17), freq=50)
FRD = PWM(Pin(16), freq=50)
RLD = PWM(Pin(7), freq=50)
RRD = PWM(Pin(8), freq=50)

speeds=[8000,13107,26214,39321,52429,65535]

def servo(angle):
    if angle>=0 and angle<=180:
        return int(1900+(angle/180)*6100)
    return servo(90)

fmotors = [FLF,RLF,FRF,RRF]
rmotors = [FLB,RLB,FRB,RRB]
Lmotors = [FLF,FLB,RLF,RLB]
Rmotors = [FRF,FRB,RRF,RRB]
def direction(deg): 
    de=int(deg/2)
    FLD.duty_u16(servo(90+deg))
    RLD.duty_u16(servo(90+deg))
    FRD.duty_u16(servo(90+deg))
    RRD.duty_u16(servo(90+deg))

def forward(s):
    for m in rmotors:
        m.duty_u16(0)
    for i in speeds[0:s+1]:
        for m in fmotors:
            m.duty_u16(i)
        utime.sleep(0.25)


def reverse(s):
    for m in fmotors:
        m.duty_u16(0)
    for i in speeds[0:s+1]:
        for m in rmotors:
            m.duty_u16(i)
        utime.sleep(0.25)

def stop(s):
    for m in rmotors:
        m.duty_u16(0)
    for m in fmotors:
        m.duty_u16(0)

def spy():
    spm.on()
    utime.sleep(1.5)
    spm.off()
        
c=[stop,forward,reverse,stop,spy]

def DO(deg,di):
    global Speed
    direction(deg)
    c[di](Speed)