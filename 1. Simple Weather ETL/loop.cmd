@echo off
:loop
    call "Weather_ETL.cmd"
    timeout /t 60 /nobreak
    goto loop
