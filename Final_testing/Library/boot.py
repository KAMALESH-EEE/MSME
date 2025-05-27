from utime import sleep
from machine import Pin

led = Pin(25,Pin.OUT)
led.on()


sleep(1)
