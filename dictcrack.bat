@echo off
setlocal enabledelayedexpansion

set essid=essid
set dictpath=C:\dicts
set hashpath=C:\Hashcat
set capfile=C:\%essid%\%essid%.hc22000

call :topath
for %%i in ( %dictpath%\*.txt ) do (
    call :crack %%i
)
pause
goto:eof

:crack
    hashcat.exe -a 0 -m 22000 -D 2 -w 1 %capfile% %~1 -O

:topath    
    %hashpath:~0,2%
    cd %hashpath%