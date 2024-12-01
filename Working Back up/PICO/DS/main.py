from machine import Pin,UART,reset
from DS import DO,Speed,spy
import _thread

import time
DO(0,0)
print('Yes')
uart = UART(0,baudrate =125000000)

led = Pin(25,Pin.OUT)


while True:
    try:
        if uart.any():
            a=uart.read()
            d=str(a).split("'")[1]
            print(d)
            addr=d[0:2]
            if addr=='01':
                if d[3] == 'r':
                    reset()
                t=d[3:]
                led.off()
                
                t=t[0:len(t)-1]
                print(f'New command:{t}')
                
                if t=='c':
                    uart.write('01_c_')
                    print('01_c_')
                    led.on()
                    time.sleep(5)
                    led.off()
                    
                if t=='01':
                    led.on()
                elif t == '02':
                    led.off()
                elif t =='s':
                    print("Yes it spray")
                    spy()
                else:
                    d=t.split(',')
                    if len(d)==2:
                        DO(int(d[0]),int(d[1]))
                    elif len(d) ==3:
                        print('speed= ',Speed)
                        Speed=int(d[2])
                        DO(int(d[0]),int(d[1]))
        time.sleep(0.5)
    except:
        print('Error')
        led.on()
