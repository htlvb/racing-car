#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from prometheus_client import start_http_server, Gauge
import time
import Adafruit_DHT

# Sensor definieren
sensor = Adafruit_DHT.DHT22

# Pin festlegen (BMC Notation)
pin = 17

# Zeit nach der wieder gesendet werden soll in Sekunden
sendepause = 3

temperatureMetric = Gauge('temperature', 'Temperature in °C')
humidityMetric = Gauge('humidity', 'Humidity in %')

start_http_server(8000)

while True:
    # Temperatur und Luftfeuchtigkeit
    feuchtigkeit, temperatur = Adafruit_DHT.read_retry( sensor, pin)
    temperatureMetric.set(temperatur)
    humidityMetric.set(feuchtigkeit)

    time.sleep( sendepause)

