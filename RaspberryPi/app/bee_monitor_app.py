import RPi.GPIO as IO
import time
from datetime import datetime 
import os
from sensor.irsensor import irsensor
import sqlite3

conn = sqlite3.connect('hivedata.db')
c = conn.cursor()

c.execute('SELECT name, type, pin FROM sensors')
sensors = []
for row in c:
    name, type, pin = row
    print('Found sensors: {0}, type: {1} on pin: {2}'.format(name, type, pin))


sensitivity = 0.0005
pin_number1 = 4       
pin_number2 = 17      
arrival = 0
departure = 0
loop1 = 1
loop2 = 1


while True:
    
    sensor1 = irsensor(pin_number1, sensitivity) 
    sensor2 = irsensor(pin_number2, sensitivity) 
    

    if (sensor1 == 1):
        time.sleep(0.1)
        
        if (sensor2 == 1 and loop1 == 1):
            departure += 1
            time_stamp = int(time.time())
            c.execute('INSERT INTO readings VALUES (?, ?, ?)',
                       (time_stamp, "out", departure))
            conn.commit()
            print ("bee_out %.0f" % departure)
            loop1 = 0
        
        elif (sensor2 == 0):
            loop1 = 1

    
            
    if (sensor2 == 1):
        time.sleep(0.1)

        if (sensor1 == 1 and loop2 == 1):
            arrival += 1
            time_stamp = int(time.time())
            c.execute('INSERT INTO readings VALUES (?, ?, ?)',
                      (time_stamp, "in", arrival))
            conn.commit()
            print ("bee_in: %.0f" % arrival)
            loop2 = 0

        elif (sensor1 == 0):
            loop2 = 1