from machine import Pin,UART,reset,PWM
from time import sleep

from Task import task,create_task
import Feild

from MyDevices import HC,DS,SM,RV,checkAll,Comm,Loop,Err,ib



print(HC)

HC.write("From HOST\n")
HC.write("Checking Communication\n")

i=1
Comm.duty_u16(ib)
for f in checkAll():
    s='0'+str(i)+str(f)
    i+=1
    HC.write(s+'\n')
tim=str(SM.Time()) 
print('Time',tim)
HC.write('Time '+tim+'\n')
Comm.duty_u16(0)
while True:
    Loop.duty_u16(ib)
    try:
        if HC.any():
            t=str(HC.read()).split("'")
            n=t[1]
            Err.duty_u16(0)
            Loop.duty_u16(0)
            
            if n == 'w':
                DS.forward()
            elif n == 's':
                DS.reverse()
            elif n == 'a':
                DS.left()
            elif n == 'd':
                DS.right()
            elif n == ' ':
                DS.stop()
                
            elif 's++' == n:
                DS.cs(1)
            elif 's--' == n:
                DS.cs(-1)
                
            elif n == 'dsr':
                DS.rst()
            elif n=='dht':
                T,h=SM.DHT()
                d=f'Tem: {T}, Hum: {h}'
                print(d)
                HC.write(d+'\n')
                
            elif n=='dis':
                h=SM.dis()
                d=f'Dis: {h} cm'
                print(d)
                HC.write(d+'\n')
            
            elif n=='pos':
                lat,lon = SM.pos()
                d=f'Lat: {lat} Lon: {lon}'
                print(d)
                HC.write(d+'\n')
                
            elif n=='spray':
                SM.Spray()
                
            elif n=='task':
                create_task()
            
            elif n=='field':
                Feild.Mode()
            
            elif n=='rst':
                reset()
                
            elif n=='err':
                Feild.non()
                
            elif n=='det':
                f=RV.detect()
                print(f)
                if f:
                    HC.write("Disease detected\n")
                else:
                    HC.write("No Disease detected\n")
                    
            elif n=='dets':
                f=RV.detect()
                print(f)
                if f:
                    HC.write("Disease detected\nFertilizer Sprayed\n")
                    SM.Spray()
                else:
                    HC.write("No Disease detected\n")
                
            elif n=='Quit':
                DS.stop()
                break
            
    except :
        Err.duty_u16(ib)
        HC.write('Error!\n')
        print('Error')
        
HC.write("Host is Exited from control\n to restart do it manually!\n")
