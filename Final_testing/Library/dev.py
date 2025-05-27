'''
File    : dev.py
Author  : Kamalesh R
Version : 0V02
created : 04/02/2025
Device  : All

This is file is Library file which includes Common operation Like communication establishment 
and common pheripheral setup
'''



from machine import Pin, UART
import utime


DATA = [0 for i in range(20)] # Data Regiters

class DEV:
    com = UART(0, baudrate = 115200)
    SlaveRegFlag = True
    Slave_Value = [[0,0,0,0],[1,0,0,0],[0,1,0,0],[1,1,0,0]] #
    SPin = [] #Slave Pin declearation added @ Rutime

    def __init__(self,ID,Name, Slave = False):
        self.ID = int(ID)
        self.Name = Name
        self.Slave = Slave
        self.BITE_Status = False 
        if Slave:
            if DEV.SlaveRegFlag:
                DEV.SetSlave()
            print(f"{self.Name} Configured as Slave")
        else:
            print(f"{self.Name} Configured as Master")

    def __str__(self):
        return (f'Device Name: {self.Name}\nID:{self.ID}')

    def Write(self,addr,data): #Fuction for Device's Reg write from Host
        cmd = str(addr)+"'w'"+str(DEV.Encode(data))
        self.Send(cmd)

    def Read(self,addr): #Fuction for Device's Reg read to Host
        cmd = str(addr)+"'r"
        return self.Send(cmd,R=True)
        
    def Send(self,data,R=False): #UART Read / Write defintion
        if self.Slave:
            DEV.S_Sel(self.ID -1)
            utime.sleep(0.01)
            DEV.com.write(data)
            print(data, "=>sent")
            utime.sleep(0.1)
            if R:
                utime.sleep(0.25)
                i=5
                data = self.Receive()
                print("Reading",end=' .')
                while (data == False):
                    if i == 0:
                        print("\nDevice not responding")
                        DEV.S_Sel(0)
                        return None
                    print(" ",end='.')
                    utime.sleep(0.5)
                    data = self.Receive()
                    i-=1
                print(f"\nReceived Data: {data}")
                DEV.S_Sel(0)
                return data 
            else:
                DEV.S_Sel(0)
        else:
            DEV.com.write(data)
            print(f"Data Sent = {data}")


    def Receive(self): # UART RX Decode
        if DEV.com.any():
            raw_data=str(DEV.com.read())
            #raw_data="b'"+input()+"'"
            print('\nRAW:'+raw_data)

            if 'b"' in raw_data:
                data=raw_data.split('"')[1].split("'")

            else:
                data = raw_data[2:-1].split("'")


            if self.Slave:              #Master read raw data
                return DEV.Decode(data[0])
            else:                           #Slave decode and response.
                if data[1] == 'r':          #read operation
                    DEV.com.write(DEV.reg_getdata(int(data[0])))
                    print("Reg Data sent")
                elif data[1] == 'w':        #write operation
                    DEV.reg_putdata(int(data[0]),data[2])
                else:
                    print("MEM R/W error occures")    
                return True            
        return False
    
    def BITE(self): # BITE() 
        self.BITE_Status=(True if(self.Read(1) == self.ID) else False)


#====== Internal Fuctions for PUT and GET data in LOCAL REG ============

    def reg_getdata(addr):
        data = DEV.Encode(DATA[addr])
        print(f"{DATA[addr]} @ {hex(addr)} reg")
        return data
    
    def reg_putdata(addr,data):
        DATA[addr] = DEV.Decode(data)
        print(f"{DATA[addr]} => {hex(addr)} reg")

 #=========================================================================
 
    def SetSlave():
        DEV.SPin = [Pin(18,Pin.OUT),Pin(19,Pin.OUT),Pin(20,Pin.OUT),Pin(21,Pin.OUT)]
        for S_dev in DEV.SPin:
            S_dev.off()
            DEV.SlaveRegFlag = False
        print("Slave Pins Configured")
    
    def S_Sel (ID):
        i=0
        for S in DEV.SPin:
            S.value(DEV.Slave_Value[ID][i])
            i+=1

    def Encode(data):           #Contruct the data with Type
        dt='s'
        if type(data) == int:
            dt = 'd'
        elif type(data) == float:
            dt = 'f'
        return str(data)+'_'+dt
    
    def Decode (data):          #Distruct the Data from Type
        t=data.split('_')
        dt=t[1]
        if dt == 'd':
            return int(t[0])
        elif dt == 'f':
            return float(t[0])
        return t[0]




