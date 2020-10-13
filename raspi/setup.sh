#!/bin/bash

sudo apt update
sudo apt install -y git

# Install Grafana (see https://grafana.com/docs/grafana/latest/installation/debian/)
sudo apt install -y apt-transport-https
sudo apt install -y software-properties-common wget
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
sudo apt update
sudo apt install -y grafana

sudo systemctl daemon-reload
sudo systemctl start grafana-server
sudo systemctl status grafana-server
sudo systemctl enable grafana-server.service

# Install docker (see https://docs.docker.com/engine/install/debian/)
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Install pip and packages
sudo apt install -y python3-pip
pip3 install prometheus_client
pip3 install Bluetin-Echo

pushd `dirname "$0"`
sudo docker run -d -p 9090:9090 -v "`pwd`/prometheus.yml:/etc/prometheus/prometheus.yml" --restart unless-stopped --network host prom/prometheus
popd
