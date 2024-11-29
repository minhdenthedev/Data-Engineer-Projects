import json
import os
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    LOG_FILE = args[0]
    OUTPUT_FILE = args[1]

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        text = f.read()

    lines = text.split("\n")[:-1]
    temperatures = []
    humidity = []
    n = len(lines)
    for line in lines:
        data = json.loads(line)['current']
        temperatures.append(data['temperature_2m'])
        humidity.append(data['relative_humidity_2m'])
    
    current = json.loads(lines[-1])['current']
    
    outputs = [
        str(current['time']),
        str(float(current['temperature_2m'])),
        str(float(max(temperatures))),
        str(float(min(temperatures))),
        str(float(sum(temperatures) / n)),
        str(float(current['relative_humidity_2m'])),
        str(float(max(humidity))),
        str(float(min(humidity))),
        str(float(sum(humidity) / n))
    ]   
    output_str = ",".join(outputs)

    if not os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            header = "time,current_temp,max_temp_last_hour,min_temp_last_hour,avg_temp_last_hour,current_humid,max_humid_last_hour,min_humid_last_hour,avg_humid_last_hour\n"
            f.write(header)
    
    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
        f.write(output_str + "\n")
    
