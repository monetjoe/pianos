@echo off
setlocal enabledelayedexpansion

set essid=wzlt
set crackpath=H:\crack\cracking
set dictfile=H:\crack\dicts\rockyou.txt
set hashpath=D:\Program Files\Hashcat
set capfile=%crackpath%\%essid%\%essid%.hc22000

call :topath
call :crack %dictfile%
pause
goto:eof

:crack
    hashcat.exe -a 0 -m 22000 -D 2 -w 1 %capfile% %~1 -O

:topath    
    %hashpath:~0,2%
    cd %hashpath%