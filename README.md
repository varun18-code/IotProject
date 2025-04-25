# IoT Temperature Logger

This project simulates an IoT system that reads temperature data (simulated or from a sensor like DHT11) and logs it to a file or MQTT/cloud platform.

## Features
- Simulated sensor using random values or actual DHT11/22 sensor on Raspberry Pi
- Logs data with timestamps
- Future scope: Push data to ThingsBoard or cloud via MQTT

## Tech Stack
- Python
- RPi.GPIO / random
- MQTT (optional)
