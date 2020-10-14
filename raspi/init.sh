#!/bin/bash

sudo passwd pi
sudo hostnamectl set-hostname racerpi1
# TODO run `sudo reboot now`

sudo apt update
sudo apt install -y git
git clone https://github.com/htlvb/racing-car.git
cd ./racing-car/raspi
