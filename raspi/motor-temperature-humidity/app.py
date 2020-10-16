#!/usr/bin/env python3

from prometheus_client import start_http_server, Gauge
import signal,sys
import time
import Adafruit_DHT

temperature_metric = Gauge('motorTemperature', 'Motor temperature in °C')
humidity_metric = Gauge('motorHumidity', 'Motor humidity in %')

start_http_server(8000)

def handle_sigterm(*args):
    sys.exit()

signal.signal(signal.SIGTERM, handle_sigterm)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 17)
    temperature_metric.set(temperature)
    humidity_metric.set(humidity)

    time.sleep(3)
