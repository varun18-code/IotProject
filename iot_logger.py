import time
import random

def get_temperature():
    return round(random.uniform(20.0, 30.0), 2)

with open("temperature_log.csv", "a") as file:
    while True:
        temp = get_temperature()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp},{temp}\n")
        print(f"Logged: {timestamp} - {temp} C")
        time.sleep(5)
