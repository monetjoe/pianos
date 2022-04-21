#! /bin/bash

pkn=$3'('$1')'
tag='/home/kali/Downloads/'$pkn'/'
if [ -d "$tag" ]; then
	rm -rf "$tag"
fi
mkdir "$tag"
echo 'kali' | sudo -S airodump-ng -c $2 --bssid $1 -w $tag$3 wlan0
echo 'kali' | sudo hcxpcapngtool -o $3.hc22000 $3-01.cap
