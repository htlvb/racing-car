# Racing car

Scripts to set up the Pi used for the racing cars.

## Raspberry Pi

The Pi reads the sensors, stores their values in a local [Prometheus](https://prometheus.io/) instance (available on port 9090) and exposes a [Grafana](https://grafana.com/) server on port 80 to visualize the sensor data.

### Setup

1. Flash [Raspberry Pi OS](https://www.raspberrypi.org/downloads/raspberry-pi-os/) on an SD card using e.g. [Etcher](https://www.balena.io/etcher/).
1. Run [configure-boot-image.ps1](raspi/configure-boot-image.ps1) to enable SSH and setup WIFI connection information.
1. Boot your Pi from the SD card.
1. Find the IP address of the Pi by checking the devices connected to your router or by using software like [Angry IP scanner](https://angryip.org/). Alternatively you can try the next step using the default host name `raspberrypi`.
1. Use [VSCode Remote SSH](https://code.visualstudio.com/docs/remote/ssh) to connect to the Pi.
1. Copy commands from [init.sh](raspi/init.sh) and run them on the Pi one by one.
1. Run [setup.sh](raspi/setup.sh).
1. Browse to [http://racerpi1:80](http://racerpi1) and log in to the dashboard using the default Grafana credentials `admin`/`admin`.
