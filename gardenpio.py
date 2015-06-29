#!/usr/bin/env python 
from time import sleep 
import RPi.GPIO as GPIO
import logging
logging.basicConfig()
from apscheduler.schedulers.blocking import BlockingScheduler

# Disables warnings and sets up type of GPIO numbering:
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Set up GPIO pins:  
sensor=[27,22,23]
sensorPow = 18
pump=[17,24,25]
for e in range(0, len(sensor)):
	GPIO.setup(pump[e], GPIO.OUT)
	GPIO.setup(sensor[e], GPIO.IN)
GPIO.setup(sensorPow, GPIO.OUT)
#power off sensor vcc to preserve the sensor electrodes:
GPIO.output(sensorPow, 0)


def irrigation():
    GPIO.output(sensorPow, 1) #power to the sensor
    sleep(1)
    print "Irrigation start"

    for e in range(0, len(sensor)):
    	while  GPIO.input(sensor[e]):  #reads sensor
            GPIO.output(pump[e], 0) #water pump reley start

    	GPIO.output(pump[e], 1) #water pump reley stop
    	GPIO.output(sensorPow, 0) #sensor power down
    print "Irrigation stop"

sched = BlockingScheduler()

# Schedules job_function to be run on every day 7  and 22 o'clock
sched.add_job(irrigation, 'cron', hour='7,21')

sched.start()

