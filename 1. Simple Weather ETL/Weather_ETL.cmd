 
@echo off
set local

:: Set API endpoint and log file
set "API_URL=https://api.open-meteo.com/v1/forecast?latitude=21.0245&longitude=105.8412&current=temperature_2m,relative_humidity_2m"
set "LOG_FILE=weather.log"
set "DB_FILE=weather.csv"

:: Fetch API data and append to log
curl -s "%API_URL%" >> "%LOG_FILE%"
echo. >> "%LOG_FILE%"

:: Use PowerShell to extract the last 60 lines and overwrite the log file
powershell -Command "(Get-Content '%LOG_FILE%' -Tail 60) | Set-Content '%LOG_FILE%'"

python transform_get_stats.py "%LOG_FILE%" "%DB_FILE%"

endlocal