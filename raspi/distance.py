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

# Fehler-Zaehler
errors = 0
response = 0

distanceMetric = Gauge('distance', 'Distance in cm')

start_http_server(8000)

def onExit(signum, frame):
    sensor.stop()
    sys.exit()

signal.signal(signal.SIGINT, onExit)

while True:
    abstand = sensor.read('cm', n)
    distanceMetric.set(abstand)

    time.sleep(sendepause)
