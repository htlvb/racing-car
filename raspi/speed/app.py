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

n = 0
dT = 0.0
t0 = time.time()
t1 = t0
speed = 0

# ---------- Callback_Lichtschranke ----------
def Callback_Lichtschranke(channel):
    global n
    n = n + 1

# Setup Lichtschranke
GPIO.setup( pin, GPIO.IN) #, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect( pin, GPIO.RISING, callback = Callback_Lichtschranke)

speedMetric = Gauge('speed', 'Speed in km/h')

start_http_server(8000)

def handle_sigterm(*args):
    GPIO.cleanup()
    sys.exit()

signal.signal(signal.SIGTERM, handle_sigterm)

while True:
    t1 = time.time()
    dT = t1 - t0
    t0 = t1
    steps = n
    rounds = steps / eventsPerRound
    speed = (rounds * circumference) / (3.6 * dT)
    n -= steps
    speedMetric.set(speed)
    
    time.sleep(sendepause)
