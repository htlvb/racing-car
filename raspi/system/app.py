#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from prometheus_client import start_http_server, Info
import time
from datetime import datetime
import signal,sys
import platform
import psutil
import socket

# Zeit nach der wieder gesendet werden soll in Sekunden
sendepause = 5

infoMetric = Info('system', 'System information')

start_http_server(8000)

def handle_sigterm(*args):
    sensor.stop()
    sys.exit()

signal.signal(signal.SIGTERM, handle_sigterm)

while True:
    info = {}
    info['system-time'] = str(datetime.now())
    info['architecture'] = platform.architecture()[0]
    info['os-version'] = platform.version()
    info['hostname'] = platform.node()
    info['platform'] = platform.platform()
    info['processor'] = platform.processor()
    info['boot-time'] = datetime.fromtimestamp(psutil.boot_time())
    info['cpu-usage'] = psutil.cpu_percent()
    info['free-ram'] = f'{round(psutil.virtual_memory().free / (1024.0 ** 3), 2)} GB'
    info['free-disk-space'] = f'{round(psutil.disk_usage("/").free / (1024.0 ** 3), 2)} GB'
    # info['ip-address-wifi'] = psutil.net_if_addrs()["wlan0"][0].address
    # info['mac-address'] = psutil.net_if_addrs()["eth0"][0].address
    info['cpu-temperature'] = psutil.sensors_temperatures()['cpu-thermal'][0].current
    infoMetric.info(info)

    time.sleep(sendepause)

