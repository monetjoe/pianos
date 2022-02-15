# wifi_tool_script
wifi cracking sh and bat

## Shell usage

0. Mount FAST150US on VMWare for Kali;
1. Drag *.sh into Kali;
2. `sh search.sh`;
3. `sh monitor.sh %tag_mac_addr% %channel% %ssid%`;
4. `sh attack.sh %tag_mac_addr% %client_mac_addr%`;
5. Once the `monitor.sh` finish handshake, stop all scripts;
6. Copy out the generated .cap file to Windows;
7. Convert the .cap package to .hc22000 on <https://hashcat.net/cap2hashcat/>;
8. Move the .hc22000 package to assigned location in crack.bat;
9. Modify the path in crack.bat and run it.

## Environment

| Linux | CUDA | hashcat |
| --- | --- | --- |
| Kali-Linux-2021.4a-vmware-amd64 | 11.4+ | 6.0.0+ |