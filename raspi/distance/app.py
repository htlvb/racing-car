#!/usr/bin/env python3

from prometheus_client import start_http_server, Gauge
import signal,sys
import time
from Bluetin_Echo import Echo

trigger_pin = 23
echo_pin = 24
sensor = Echo(trigger_pin, echo_pin)

distanceMetric = Gauge('distance', 'Distance in cm')

start_http_server(8000)

def handle_sigterm(*args):
    sensor.stop()
    sys.exit()

signal.signal(signal.SIGTERM, handle_sigterm)

while True:
    distance = sensor.read('cm', samples = 5)
    distanceMetric.set(distance)

    time.sleep(0.5)
