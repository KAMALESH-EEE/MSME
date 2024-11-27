import machine
import time
from HC_SR04 import HCSR04

led = machine.Pin(25,machine.Pin.OUT)
us_sensor = HCSR04(trigger_pin=18, echo_pin=19, echo_timeout_us=10000)
led.on()
time.sleep(5)
led.off()

