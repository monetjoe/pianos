@echo off
setlocal enabledelayedexpansion

set essid=essid
set masks[0]=?d?d?d?d?d?d?d?d?d?d?d
set masks[1]=?d?d?d?d?d?d?d?d?d?d?d
@REM ...
@REM set masks[n]=?d?d?d?d?d?d?d?d?d?d?d

set hashpath=C:\Hashcat
set capfile=C:\%essid%\%essid%.hc22000

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