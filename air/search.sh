#! /bin/bash

rm -rf search
mkdir search
echo 'kali' | sudo -S airodump-ng wlan0 -w search/search