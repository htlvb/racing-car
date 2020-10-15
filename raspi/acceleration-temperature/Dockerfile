FROM python:3

RUN pip3 install prometheus_client RPi.GPIO adafruit-circuitpython-mpu6050
WORKDIR /usr/src/app
COPY app.py ./

CMD [ "python", "./app.py" ]
