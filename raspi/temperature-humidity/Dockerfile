FROM python:3

RUN pip3 install prometheus_client Adafruit_DHT
WORKDIR /usr/src/app
COPY app.py ./

CMD [ "python", "./app.py" ]
