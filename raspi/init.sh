#!/bin/bash

# Set password
sudo passwd pi

# Set host name
sudo sed -i 's/raspberrypi/racerpi1/g' /etc/hosts
sudo sed -i 's/raspberrypi/racerpi1/g' /etc/hostname
sudo systemctl restart systemd-logind.service
sudo hostnamectl --static --transient --pretty set-hostname racerpi1

# Clone git repository
sudo apt update
sudo apt install -y git
git clone https://github.com/htlvb/racing-car.git
cd ./racing-car/raspi
