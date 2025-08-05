import machine, time, utime
from machine import Pin

class HCSR04:

    def __init__(self, trigger_pin, echo_pin, echo_timeout_us=500*2*30):
        
        self.trigger_pin = Pin(trigger_pin, Pin.OUT)
        self.echo_pin = Pin(echo_pin, Pin.IN)

    def distance(self):
        self.trigger_pin.value(0)
        utime.sleep_us(2)
        self.trigger_pin.value(1)
        utime.sleep_us(10)
        self.trigger_pin.value(0)

        start_time = utime.ticks_ms()
        while self.echo_pin.value() == 0:
            if utime.ticks_diff(utime.ticks_ms(), start_time) > 5000:
                return None
        pulse_start = utime.ticks_us()
        
        start_time = utime.ticks_ms()
        while self.echo_pin.value() == 1:
            if utime.ticks_diff(utime.ticks_ms(), start_time) > 5000:
                return None
        pulse_end = utime.ticks_us()
        pulse_duration = utime.ticks_diff(pulse_end, pulse_start)
        
        distance_cm = pulse_duration / 58
        
        return distance_cm
