import machine
import time

led = machine.Pin(25,machine.Pin.OUT)

led.on()
time.sleep(5)
led.off()