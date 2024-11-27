from machine import Pin,UART,PWM
import time as t

com = UART(0,tx =Pin(0),rx = Pin(1), baudrate=125000000)

HC = UART(1, tx =Pin(4),rx = Pin(5), baudrate=9600)

led = Pin(25,Pin.OUT)

RVdet = Pin(16,Pin.OUT)
RVdet.off()
RVres = Pin(17,Pin.IN)

ib=15000

Comm = PWM(Pin(7))
Comm.freq(50)
Comm.duty_u16(0)
Loop= PWM(Pin(6))
Loop.freq(50)
Loop.duty_u16(0)
Err = PWM(Pin(8))
Err.freq(50)
Err.duty_u16(0)


class DS:
    Id='01'
    
    global com,t

    def check():
        com.read()
        com.write('01_c_')
        Comm.duty_u16(ib)
        for i in range(10):
            if com.any():
                k=str(com.read() )
                if k == "b'01_c_'":
                    Comm.duty_u16(0)
                    return True
            t.sleep(1)
        Comm.duty_u16(0)
        return False
    def rst():
        com.write('01_r_')
                
        
    def stop():
        data="01_00,00_"
        com.write(data)

    def forward():
        data="01_0,01_"
        print('Forward')
        com.write(data)
    
    def reverse():
        data="01_0,02_"
        print('Reverse')
        com.write(data)

    def left():
        data="01_-90,01_"
        com.write(data)

    def right():
        data="01_90,01_"
        com.write(data)

    def move(n):
        com.write('01_'+str(n)+'_')
        
    def cs(n):
        com.write('01_cs_'+str(n)+'_')



class SM:
    global com
    Id='02'

    def check():
        Comm.duty_u16(ib)
        com.read()
        com.write('02_c_')
        for i in range(10):
            if com.any():
                k=str(com.read())
                #print(k)
                if k == "b'02_c_'":
                    Comm.duty_u16(0)
                    return True
            t.sleep(1)
        Comm.duty_u16(0)
        return False
                

    def DHT():
        data='02_0_'
        print('getting DHT data')
        Comm.duty_u16(ib)
        com.write(data)
        for i in range(100):
            if com.any():
                d=str(com.read()).split("'")[1]
                print(d)
                datas = d.split('_')
                #print(datas)
                if datas[0] == '02':
                    Comm.duty_u16(0)
                    return eval(datas[1])
            t.sleep(0.1)
        else:
            Comm.duty_u16(0)
            return None,None
        
        

    def dis():
        data='02_1_'
        Comm.duty_u16(ib)
        com.write(data)
        for i in range(100):
            if com.any():
                d=str(com.read()).split("'")[1]
                datas = d.split('_')
                #print(datas)
                if datas[0] == '02':
                    print(datas[1])
                    Comm.duty_u16(0)
                    return float(datas[1])
            t.sleep(0.1)
        else:
            Comm.duty_u16(0)
            return None
        
    def pos():
        data='02_2_'
        #print('getting GPS data')
        Comm.duty_u16(ib)
        com.write(data)
        for i in range(100):
            if com.any():
                d=str(com.read()).split("'")[1]
                datas = d.split('_')
                #print(datas)
                if datas[0] == '02':
                    Comm.duty_u16(0)
                    print(datas[1])
                    return eval(datas[1])
            t.sleep(0.1)
        else:
            Comm.duty_u16(0)
            return None,None

    def Time():
        data='02_3_'
        print('getting RTC data')
        com.write(data)
        Comm.duty_u16(ib)
        for i in range(100):
            if com.any():
                d=str(com.read()).split("'")[1]
                datas = d.split('_')
                #print(datas)
                if datas[0] == '02':
                    Comm.duty_u16(0)
                    return datas[1]
            t.sleep(0.1)
        else:
            Comm.duty_u16(0)
            return None
        
    def Spray():
        com.write('02_4_')
        
class RV:
    global RVdet,RVres
    Id='03'
    
    def stop():
        com.write('03_stop_')
        
    def detect():
        RVdet.on()
        Comm.duty_u16(ib)
        t.sleep(1)
        RVdet.off()
        for i in range(10):
            de=RVres.value()
            if de==1:
                Comm.duty_u16(0)
                return True
            t.sleep(1)
        Comm.duty_u16(0)
        return False
        

def checkAll():
    global com,t
    devices=[DS,SM]
    s=[]
    for device in devices:
        f=device.check()
        print(device.Id,f)
        s.append(f)
    return s

def Input(s):
    HC.write(s+'\n')
    while not (HC.any()):
        pass
    t=str(HC.read()).split("'")
    return t[1]

def Print(s):
    HC.write(s+'\n')
    
    