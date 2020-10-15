FROM python:3

RUN pip3 install prometheus_client RPi.GPIO adafruit-circuitpython-ads1x15
WORKDIR /usr/src/app
COPY app.py ./

CMD [ "python", "./app.py" ]
