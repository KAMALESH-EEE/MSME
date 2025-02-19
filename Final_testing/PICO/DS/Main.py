from DEVICES import *

while True:
    
    if HOST.Receive():
        LED.on()
        CMD[DATA[5]](DATA[6])
        LED.off()

    else:
        LED.off()
    utime.sleep(0.1)


    

    
