@echo off
setlocal enabledelayedexpansion

set masks[0]=1?d?d0429?d?d?d?d
set masks[1]=1?d?d4290?d?d?d?d
set masks[2]=0429?d?d?d?d?d?d?d
set masks[3]=?d?d?d?d?d?d?d?d
set masks[4]=1?d?d?d?d?d?d?d?d?d?d

set /p essid=<.\config\essid.txt
set /p dictpath=<.\config\dictpath.txt
set /p crackpath=<.\config\crackpath.txt
set /p hashpath=<.\config\hashpath.txt
set capfile=%crackpath%\%essid%\%essid%.hc22000

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