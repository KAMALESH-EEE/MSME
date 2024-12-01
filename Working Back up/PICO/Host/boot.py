from machine import Pin
import time

led = Pin(25,Pin.OUT)
led.on()

time.sleep(5)
led.off()
