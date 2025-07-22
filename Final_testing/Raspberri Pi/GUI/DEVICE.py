
'''
File    : dev.py
Author  : Kamalesh R
Version : 0V02
created : 22/07/2025
Device  : All

This is file is Library file which includes Common operation Like communication establishment 
and common pheripheral setup
'''


import serial
import time as utime
from time import sleep
from Field import Field_List,Field_Close




DATA = [0 for i in range(20)] # Data Regiters

class DEV:
    com = None
    #com = serial.Serial('/dev/ttyAMA0', 115200, timeout=1)
    #com.flush()
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
        #DEV.SPin = [Pin(18,Pin.OUT),Pin(19,Pin.OUT),Pin(20,Pin.OUT),Pin(21,Pin.OUT)]
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

#=============***********=========================
#=================GUI==============================
import tkinter as tk
from tkinter import messagebox

Task_List = ['Spray','Plant']



Field_add_window=None
Main_Window = None

# Save the list of objects to a file


Titel="Field"
BG="lightgreen"

def SetTask(T,window):

    global Main_Window , Field_add_window
    Main_Window = window


    Field_add_window = tk.Toplevel(Main_Window,bg=BG)  # Create a new window
    Field_add_window.geometry("300x200")  # Set dimensions for the subwindow
    Field_add_window.title(Titel)

    # Add a button to the subwindow

    bottom_menu = tk.Frame(Field_add_window, bg=BG, height=10)
    bottom_menu.pack(side="bottom", fill="x")
    tk.Label(Field_add_window, text="Select an Crop", font=("Arial", 12), bg=BG, fg="darkblue").pack(pady=5, padx=10, anchor="w")

    options = [i.Name for i in Field_List]
    dropdown_var = tk.StringVar()
    dropdown_var.set(options[0])  # Set default value
    dropdown_menu = tk.OptionMenu(Field_add_window, dropdown_var, *options)
    dropdown_menu.pack(pady=5)


    tk.Button(Field_add_window, text="Do Task",font=("Arial", 14), command=lambda:DO_TASK(T,dropdown_var.get(),window)).pack(pady=10, padx=10)

    tk.Button(bottom_menu, text="Exit", font=("Arial", 14), command=lambda: Field_add_window.destroy()).pack(side="left", padx=20)
  
def DO_TASK(T,F,window):
    try:
    
        global Sub_window
        for i in Field_List:
            if i.Name == F:
                obj = i
                break
        print(obj.Crop,T)
        Main_Name1 = tk.Label(window, text="Loading Task...", font=("Arial", 10), bg=BG, fg="red")
        Main_Name1.pack(pady=2)
        re = USER_DD(T,obj)
        if re:
            Main_Name1 = tk.Label(window, text="Task Loaded Sucessfully", font=("Arial", 10), bg=BG, fg="green")
            Main_Name1.pack(pady=2)
            sleep(2)
            window.quit()
            print('Control through Remote')
  
    except:
       print("Error")
       Field_Close("Error",Field_add_window)






#==========================================







#========= HOST decleration ==============

HOST = DEV(0,'HOST')

DATA[0] = 'Disease Detector'
DATA[1] = 1

#++++++++++++++++++++++++++++++++++++++++++

  
'''
    Registers Details:
    0 to 4 :Reserved
    5: Host control {0->RV as Slave, 1-> RV as Temp Host, 2 -> Waiting respose from HOST, 3 -> Respose from Host}
    6: Disease Detection
    7: Detection Status {0->Not started, DD-> disease detected, DN-> Not detected, W-> still detecting}
    8: Robot pos in feild
    10: CMD {RAW- Raw read/write, REG -> REG R/W, <TASK Name> -> Task (Plant,Spray)}
    11: Feild Name
    12: ROW size
    13: COL size
    14: Crop
    16: RAW read/write
    18: ADDRESS of HOST REG
    19: DATA to HOST
'''

'''
    HOST Register Details:
    0 to 4 :Reserved
    5: Host control {0->RV as Slave, 1-> RV as Temp Host, 2 -> in Task Mode}
    6: Control Reg {HC->User control, Task-> Task assigned,}
    7: Task Reg {None,plant,disease_det,fert_spray}
    8: Field Details
    9: 
'''
def Check():
    pass

#=========DD Connect==================

def USER_DD(T,F):

    DATA[5] = 2
    while True:
        HOST.Receive()
        sleep(0.2) 
        if DATA[5] == 0:
            return False
        elif DATA[5] == 1:
            break
        elif DATA[5] == 3:
            Check()
         
    
    DATA[11] = F.Name
    DATA[12] = F.row
    DATA[13] = F.col
    DATA[14] = F.Crop
    DATA[10]  = T
    DATA[5]  = 2

    while True:
        HOST.Receive()
        sleep(0.2) 
        if DATA[5] == 0:
            return False
        elif DATA[5] == 1:
            return True
        elif DATA[5] == 3:
            Check()
            return False




