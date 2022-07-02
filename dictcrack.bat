@echo off
setlocal enabledelayedexpansion

set /p essid=<.\config\essid.txt
set /p dictpath=<.\config\dictpath.txt
set /p crackpath=<.\config\crackpath.txt
set /p hashpath=<.\config\hashpath.txt
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