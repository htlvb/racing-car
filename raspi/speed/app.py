#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from prometheus_client import start_http_server, Gauge
import math
import signal,sys
import time
import RPi.GPIO as GPIO

# GPIO-Setup
GPIO.setmode( GPIO.BCM) # GPIO Nummern statt Board Nummern
# Pin setzen
pin = 25

# Zeit nach der wieder gesendet werden soll in Sekunden
sendepause = 0.5

eventsPerRound = 20
diameter = 0.110 # m
circumference = diameter * math.pi

# ---------- Callback_Lichtschranke ----------
def Callback_Lichtschranke( channel):
    isMoving = True

    if n >= eventsPerRound:
        t1 = time.time()
        dT = t1 - t0
        t0 = t1
        speed = (1 / diameter) * dT / 3.6
        n -= eventsPerRound

# Setup Variablen
n = 0
freq = 0.0
dT = 0.0
rpm = 0.0
t0 = time.time()
isMoving = False

# Setup Lichtschranke
GPIO.setup( pin, GPIO.IN) #, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect( pin, GPIO.RISING, callback = Callback_Lichtschranke, bouncetime=2)

speedMetric = Gauge('speed', 'Speed in km/h')

start_http_server(8000)

def handle_sigterm(*args):
    GPIO.cleanup()
    sys.exit()

signal.signal(signal.SIGTERM, handle_sigterm)

while True:
    if not isMoving:
        speedMetric.set(0)
    else:
        speedMetric.set(rpm)
    isMoving = False
    time.sleep(sendepause)
