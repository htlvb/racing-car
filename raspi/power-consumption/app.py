#!/usr/bin/env python3

from prometheus_client import start_http_server, Gauge
import signal,sys
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c, gain = 2/3)
chan = AnalogIn(ads, ADS.P0)

acs_scale_factor = 0.066 # Volt/Ampere, see https://components101.com/sensors/acs712-current-sensor-module

power_consumption_metric = Gauge('powerConsumption', 'Power consumption in A')

start_http_server(8000)

def handle_sigterm(*args):
    sys.exit()

signal.signal(signal.SIGTERM, handle_sigterm)

while True:
    # see https://components101.com/sensors/acs712-current-sensor-module
    power_consumption = -(chan.voltage - 2.5) / acs_scale_factor
    power_consumption_metric.set(power_consumption)

    time.sleep(1)

