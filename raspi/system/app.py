#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from prometheus_client import start_http_server, Gauge, Info
import time
from datetime import datetime
import signal,sys
import platform
import psutil
import socket

# Zeit nach der wieder gesendet werden soll in Sekunden
sendepause = 5

infoMetric = Info('system', 'System information')
cpuUsageMetric = Gauge('cpuUsage', 'CPU usage in %')
freeRamMetric = Gauge('freeRam', 'Free RAM in GB')
freeDiskSpaceMetric = Gauge('freeDiskSpace', 'Free disk space in GB')
cpuTemperatureMetric = Gauge('cpuTemperature', 'CPU temperature in °C')

start_http_server(8000)

def handle_sigterm(*args):
    sys.exit()

signal.signal(signal.SIGTERM, handle_sigterm)

while True:
    info = {}
    info['systemTime'] = str(datetime.now())
    info['architecture'] = platform.architecture()[0]
    info['osVersion'] = platform.version()
    info['hostname'] = platform.node()
    info['platform'] = platform.platform()
    info['processor'] = platform.processor()
    info['bootTime'] = str(datetime.fromtimestamp(psutil.boot_time()))
    # info['ipAddressWifi'] = psutil.net_if_addrs()["wlan0"][0].address
    # info['macAddress'] = psutil.net_if_addrs()["eth0"][0].address
    infoMetric.info(info)

    cpuUsageMetric.set(psutil.cpu_percent())
    freeRamMetric.set(psutil.virtual_memory().free / (1024.0 ** 3))
    freeDiskSpaceMetric.set(psutil.disk_usage("/").free / (1024.0 ** 3))
    cpuTemperatureMetric.set(psutil.sensors_temperatures()['cpu-thermal'][0].current)

    time.sleep(sendepause)

