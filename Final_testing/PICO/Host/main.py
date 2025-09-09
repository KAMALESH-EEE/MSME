
from machine import UART
import time

from DEVICES import *
from Feild import Fields as Fi
import DEVICES as Dev
from utime import sleep

Dev.Fields = Fi

for i in range(21,20):
    print(_DD.Read(i))
    time.sleep(1)
Print('System Booted')
DD.USER_DD()
