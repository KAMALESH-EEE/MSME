from machine import Pin,UART
from SM import sen,led
import time


uart = UART(0,baudrate =125000000)

sen_data=[]
com=[]



def collect_all_data():
    global sen_data
    sd=[]
    for i in sen:
        sd.append(i())
    sen_data=sd
    print(sen_data)

def CoM():
    global com,uart
    while True:
        if uart.any():
            a=uart.read()
            d=str(a).split("'")[1]
            print(d)
            addr=d[0:2]
            if addr=='02':
                d=d[3:len(d)-1]
                print(d)
                if d=='c':
                    uart.write('02_c_')                
                else:
                    i=int(d)
                    com.append(i)
                
#_thread.start_new_thread(CoM, ())

while True:
    try:
        
        if uart.any():
            a=uart.read()
            s=str(a).split("'")[1]
            print(s)
            addr=s[0:2]
            if addr=='02':
                s=s[3:len(s)-1]
                print(s)
                if s=='c':
                    uart.write('02_c_')                
                else:
                    c=int(s)
                    led.off()
                    d=str(sen[c]())
                    print(d)
                    d='02_'+d+'_'
                    print(d)
                    uart.write(d)
        time.sleep(0.1)

    except:
         led.on()
         print('Error')
         
        
    
