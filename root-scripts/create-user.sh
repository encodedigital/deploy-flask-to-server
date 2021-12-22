#!/bin/bash

#Setting up user on brand new VPS
apt -y update && apt -y upgrade
tput setaf 6; echo "Create Username:"
tput setaf 7;
read username
if id "$username" &>/dev/null; then
    tput setaf 6; echo 'User already exists'
    tput setaf 7;
else
    adduser $username
    adduser $username sudo
    addgroup sftp
    adduser $username sftp
fi
