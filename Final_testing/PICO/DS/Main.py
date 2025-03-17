from DEVICES import *

while True:
    
    if HOST.Receive():
        LED.on()
        if not (DATA[8] == DATA[7]):
            Steering(FSD)
        CMD[DATA[5]](DATA[6])
        LED.off()

    else:
        LED.off()
    utime.sleep(0.1)


    

    
