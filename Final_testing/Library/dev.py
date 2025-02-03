from machine import Pin, UART
import utime


DATA = [0 for i in range(20)]
DATA[0] = 'HOST'
DATA[1] = 'A'

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
        
    def Write_Data(self,data,R=False):
        if self.Slave:
            DEV.S_Sel(self.ID)
            utime.sleep(0.01)
            DEV.com.write(data)
            utime.sleep(0.1)
            print("Data sent")
            if R:
                utime.sleep(1)
                i=5
                data = self.Read_Data()
                print("Reading",end=' .')
                while (data == False):
                    if i == 0:
                        print("\nDevice not responding")
                        DEV.S_Sel(0)
                        return None
                    print(" ",end='.')
                    utime.sleep(1)
                    data = self.Read_Data()
                    i-=1
                print(f"\nData:{data}")
                DEV.S_Sel(0)
                return data 
            else:
                DEV.S_Sel(0)
        else:
            DEV.com.write(data)
            print(f"Data Sent = {data}")


    def Read_Data(self):
        if DEV.com.any():
            data=DEV.com.read()
            if not self.Slave:          #Master read raw data
                return str(data).split("'")[1]
            else:
                pass            #Slave decode and response.
        return False
            
 
 
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
