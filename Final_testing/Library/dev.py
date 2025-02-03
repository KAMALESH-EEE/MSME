from machine import Pin, UART
import utime

class DEV:
    com = UART(0, buadrate = 115200)
    SlaveRegFlag = True
    Slave_Value = [[0,0,0,0],[1,0,0,0],[0,1,0,0],[1,1,0,0]]
    SPin = []

    def __init__(self,ID,Name, Slave = False):
        self.ID = int(ID)
        self.Name = Name
        self.Slave = Slave
        if Slave:
            if DEV.SlaveRegFlag:
                DEV.SetSlave()
            print("Slave Device Configured")
        else:
            print("Master Device Configured")

    def __str__(self):
        print(f'Device Name: {self.Name}\nID:{self.ID}')
        
    def write_data(self,data):
        if self.Slave:
            DEV.S_Sel(self.ID)
            utime.sleep(0.01)
            DEV.com.write(data)
            utime.sleep(0.1)
            DEV.S_Sel(0)
        else:
            DEV.com.write(data)
        print(f"Data Sent = {data}")

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
