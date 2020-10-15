#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from prometheus_client import start_http_server, Gauge
import signal,sys
import math
import time
import board
import busio
import adafruit_mpu6050

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_mpu6050.MPU6050(i2c)

# Zeit nach der wieder gesendet werden soll in Sekunden
sendepause = 0.5

accelerationMetric = Gauge('acceleration', 'Acceleration in m/s2')
temperatureMetric = Gauge('temperature', 'Temperature in °C')

start_http_server(8000)

def handle_sigterm(*args):
    sys.exit()

signal.signal(signal.SIGTERM, handle_sigterm)

while True:
    (accel_x, accel_y, accel_z) = sensor.acceleration
    totalAcceleration = math.sqrt(accel_x * accel_x + accel_y * accel_y + accel_z * accel_z)
    accelerationMetric.set(totalAcceleration)

    temperatureMetric.set(sensor.temperature)

    time.sleep(sendepause)
