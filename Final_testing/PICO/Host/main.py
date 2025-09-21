
from machine import UART
import time

from DEVICES import *
from Feild import Fields as Fi
import DEVICES as Dev
from utime import sleep

Dev.Fields = Fi


Print('System Booted')
DD.USER_DD()
