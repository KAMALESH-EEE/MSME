from machine import Pin
import utime
Led = Pin(25,Pin.OUT)
Led.on()
print("BOOTING",end=' ')
for i in range(10):
    print(".",end=' ')
    utime.sleep(1)
print("\nModule Booted Sucessfuly!")
Led.off()
