# wifi_tool_script
Wifi cracking sh and bat scripts

## Usage
0. Mount FW150US to Kali in VMware
1. Drag `*.sh` into Kali and open a terminal at its path
2. Run `sh find.sh`
3. Run `sh see.sh %tag_mac_addr% %channel% %ssid%`
4. Run `sh atk.sh %tag_mac_addr% %client_mac_addr%` (Or Run `sh atkall.sh %tag_mac_addr%` to deauth all)
5. Once the `see.sh` finish handshake, stop all scripts
6. Copy the generated `.cap` file to Windows
7. Convert the `.cap` package to `.hc22000` on <a href='https://hashcat.net/cap2hashcat' target='_blank'>cap2hashcat</a>
8. Move the `.hc22000` package to assigned location in `crack.bat`
9. Modify paths in `./config` and run it

## Notes
`reg.sh` is used to register `hcxpcapngtool`, if you do not want to convert .cap by cap2hashcat website, this tool can help you convert it locally;

`format.sh` is used to fix encode format bugs caused by moving scripts from Linux to Windows;

`show.sh` is used to make monitored wifis fixed into a log to make copying their info more easily.

## Dir structure
- wifi-tool
  - air
    - *.sh
    - hcxpcapngtool
  - config
    - crackpath.txt
    - dictpath.txt
    - essid.txt
    - hashpath.txt
  - cracked
    - wifi1
      - wifi1.hc22000
      - wifi1.txt
    - ...
  - cracking
    - wifi2
      - wifi2.hc22000
    - ...
  - dicts
    - rockyou.txt
    - ...
  - crack.bat
  - dictcrack.bat
