#!/usr/bin/env python3

from prometheus_client import start_http_server, Gauge, Info
import time
from datetime import datetime
import signal,sys
import platform
import psutil
import socket

info_metric = Info('system', 'System information')
cpu_usage_metric = Gauge('cpuUsage', 'CPU usage in %')
free_ram_metric = Gauge('freeRam', 'Free RAM in GB')
free_disk_space_metric = Gauge('freeDiskSpace', 'Free disk space in GB')
cpu_temperature_metric = Gauge('cpuTemperature', 'CPU temperature in °C')

start_http_server(8000)

def handle_sigterm(*args):
    sys.exit()

signal.signal(signal.SIGTERM, handle_sigterm)

while True:
    info = {}
    # TODO doesn't work well within a container
    info['systemTime'] = str(datetime.now())
    info['architecture'] = platform.architecture()[0]
    info['osVersion'] = platform.version()
    info['hostname'] = platform.node()
    info['platform'] = platform.platform()
    info['processor'] = platform.processor()
    info['bootTime'] = str(datetime.fromtimestamp(psutil.boot_time()))
    # info['ipAddressWifi'] = psutil.net_if_addrs()["wlan0"][0].address
    # info['macAddress'] = psutil.net_if_addrs()["eth0"][0].address
    info_metric.info(info)

    cpu_usage_metric.set(psutil.cpu_percent())
    free_ram_metric.set(psutil.virtual_memory().free / (1024.0 ** 3))
    free_disk_space_metric.set(psutil.disk_usage("/").free / (1024.0 ** 3))
    cpu_temperature_metric.set(psutil.sensors_temperatures()['cpu-thermal'][0].current)

    time.sleep(5)

