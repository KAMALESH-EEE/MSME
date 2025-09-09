from DEVICES import *
import utime

while True:
    
    if HOST.Receive():
        LED.on()
        if not (DATA[8] == DATA[7]):
            Steering(FSD)
        CMD[DATA[5]](DATA[6])
        utime.sleep(0.5)
        Fun_Spray()
        LED.off()

    else:
        LED.off()
    utime.sleep(0.1)