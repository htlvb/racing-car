#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from prometheus_client import start_http_server, Gauge
import signal,sys
import time
import RPi.GPIO as GPIO

# GPIO-Setup
GPIO.setmode( GPIO.BCM) # GPIO Nummern statt Board Nummern
# Pin setzen
pin = 25

# Zeit nach der wieder gesendet werden soll in Sekunden
sendepause = 0.5

# nach N Signalen rpm_N berechnen
N = 30

# Schlitzanzahl
S = 20

# ---------- Callback_Lichtschranke ----------
def Callback_Lichtschranke( channel):
    global t0, freq, dT, rpm
    global n, N, S
    global t0_N, freq_N, dT_N, rpm_N

    t1 = time.time()
    dT = t1 - t0
    freq = 1.0 / (S * float( dT))
    rpm = freq * 60

    t0 = t1

    n = n + 1

    if n > N:
        dT_N = (t1 - t0_N) / float( N)
        freq_N = 1.0 / (S * float( dT_N))
        rpm_N = freq_N * 60

        t0_N = t1

        n = 0

# Setup Variablen
freq = 0.0
dT = 0.0
rpm = 0.0

n = 0
freq_N = 0.0
dT_N = 0.0
rpm_N = 0.0

# Setup Lichtschranke
GPIO.setup( pin, GPIO.IN) #, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect( pin, GPIO.RISING, callback = Callback_Lichtschranke, bouncetime=2)

speedMetric = Gauge('speed', 'Speed in km/h')
smoothedSpeedMetric = Gauge('smoothedSpeed', 'Speed in km/h - smoothed')

start_http_server(8000)

def handle_sigterm(*args):
    GPIO.cleanup()
    sys.exit()

signal.signal(signal.SIGTERM, handle_sigterm)

# ---------- t0 bestimmen ----------
t0 = time.time()
t0_N = t0

while True:
    speedMetric.set(rpm)
    smoothedSpeedMetric.set(rpm_N)

    time.sleep(sendepause)
