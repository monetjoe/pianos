@echo off
setlocal enabledelayedexpansion

set essid=wzlt
set masks[0]=1?d?d0429?d?d?d?d
set masks[1]=1?d?d4290?d?d?d?d
set masks[2]=0429?d?d?d?d?d?d?d
set masks[4]=?d?d?d?d?d?d?d?d
set masks[3]=1?d?d?d?d?d?d?d?d?d?d

set hashpath=D:\Program Files\Hashcat
set capfile=H:\crack\%essid%\%essid%.hc22000

set len=0
:SymLoop
if defined masks[%len%] (
    set /a "len+=1"
    GOTO :SymLoop
)
set /a "len-=1"
call :topath
for /l %%n in (0,1,%len%) do (
    call :crack !masks[%%n]!
)
pause
goto:eof

:crack
    hashcat.exe -a 3 -m 22000 -D 2 -w 1 %capfile% %~1 -O

:topath  
    %hashpath:~0,2%
    cd %hashpath%