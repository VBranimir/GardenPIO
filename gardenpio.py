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
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.IN)
sensor = 27
sensorPow = 18
pump = 17

#power off sensor vcc to preserve the sensor electrodes:
GPIO.output(sensorPow, 0)

def irrigation():
    GPIO.output(sensorPow, 1) #power to the sensor
    sleep(1)
    print "Irrigation start"
    while  GPIO.input(sensor):  #reads sensor
                GPIO.output(pump, 0) #water pump reley start

    GPIO.output(pump, 1) #water pump reley stop
    GPIO.output(sensorPow, 0) #sensor power down
    print "Irrigation stop"

sched = BlockingScheduler()

# Schedules job_function to be run on every day 7  and 22 o'clock
sched.add_job(irrigation, 'cron', hour='7,22')

sched.start()

