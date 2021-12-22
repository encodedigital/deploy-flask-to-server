#!/bin/bash

#Set-up firewall
sudo apt install ufw
sudo ufw default allow outgoing
sudo ufw default deny incoming

sudo ufw allow ssh
sudo ufw allow 80
sudo ufw allow 443

sudo ufw enable

#Give sftp access to only user
sudo chmod 700 /home/$USER/


#Installing Docker
sudo apt-get update
sudo apt-get -y install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose

