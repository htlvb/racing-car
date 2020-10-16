#!/usr/bin/env python3

from prometheus_client import start_http_server, Gauge
import math
import signal,sys
import time
import RPi.GPIO as GPIO

events_per_round = 20
diameter = 0.110 # m
circumference = diameter * math.pi

n = 0
dt = 0.0
t0 = time.time()
t1 = t0
speed = 0

def tick(channel):
    global n
    n = n + 1

GPIO.setmode(GPIO.BCM)
pin = 25
GPIO.setup(pin, GPIO.IN)
GPIO.add_event_detect(pin, GPIO.RISING, callback = tick)

speed_metric = Gauge('speed', 'Speed in km/h')

start_http_server(8000)

def handle_sigterm(*args):
    GPIO.cleanup()
    sys.exit()

signal.signal(signal.SIGTERM, handle_sigterm)

while True:
    t1 = time.time()
    dt = t1 - t0
    t0 = t1
    steps = n
    rounds = steps / events_per_round
    speed = (rounds * circumference) / (3.6 * dt)
    n -= steps
    speed_metric.set(speed)
    
    time.sleep(0.5)
