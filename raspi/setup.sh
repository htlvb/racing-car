#!/bin/bash

sudo apt update
sudo apt install -y git

# Set host name
sudo hostnamectl set-hostname racerpi1
# TODO sudo reboot now

# Install pip
sudo apt install -y python3-pip

# Install docker (see https://docs.docker.com/engine/install/debian/)
# curl -fsSL https://get.docker.com -o get-docker.sh
# sudo sh get-docker.sh
curl -fsSL https://download.docker.com/linux/raspbian/gpg | sudo apt-key add -
echo "deb [arch=armhf] https://download.docker.com/linux/raspbian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker-ce.list
sudo apt update
sudo apt install -y docker-ce
sudo pip3 install docker-compose

# Run app
docker-compose up -d
