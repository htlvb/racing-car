FROM python:3

WORKDIR /usr/src/app
COPY app.py ./
RUN pip3 install prometheus_client Adafruit_DHT

CMD [ "python", "./app.py" ]
