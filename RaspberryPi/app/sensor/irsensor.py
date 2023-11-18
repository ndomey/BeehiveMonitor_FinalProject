import RPi.GPIO as IO
import time
from time import sleep
from datetime import datetime 
import os


IO.setmode(IO.BCM)
IO.setwarnings(False)

def set_up_sensor(pin_number):

    IO.setup(pin_number, IO.OUT)
    IO.output(pin_number, IO.HIGH)
    time.sleep(0.01)
    charging_stop = 0
    charging_start = time.time()
    IO.setup(pin_number, IO.IN, pull_up_down=IO.PUD_DOWN)

    while IO.input(pin_number) > 0:
        pass
    if IO.input(pin_number) == 0:
        charging_stop = time.time()

    charging_time = charging_stop - charging_start
    return charging_time


def irsensor(pin_number, sensitivity):
    
    if set_up_sensor(pin_number) < sensitivity:
        sensor_status = 1
    else:
        sensor_status = 0
    return sensor_status
