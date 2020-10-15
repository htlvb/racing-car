#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from prometheus_client import start_http_server, Gauge
import signal,sys
import time
from Bluetin_Echo import Echo

# Pins festlegen (BMC Notation)
trigger_pin = 23
echo_pin = 24

# Anzahl der Messungen für ein Ergebnis
n = 5

# Schallgeschwindigkeit
schallgeschw = 315

# Sensor definieren
sensor = Echo(trigger_pin, echo_pin, schallgeschw)

# Zeit nach der wieder gesendet werden soll in Sekunden
sendepause = 0.5

distanceMetric = Gauge('distance', 'Distance in cm')

start_http_server(8000)

def handle_sigterm(*args):
    sensor.stop()
    sys.exit()

signal.signal(signal.SIGTERM, handle_sigterm)

while True:
    abstand = sensor.read('cm', n)
    distanceMetric.set(abstand)

    time.sleep(sendepause)
