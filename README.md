# OpenWeather ETL Pipeline on AWS EC2
This project demonstrates a basic ETL pipeline that extracts real-time weather data 
from the OpenWeather API, processes timestamp and timezone information correctly, 
and prepares the data for downstream analytics.

The pipeline is executed on an AWS EC2 Ubuntu instance and version-controlled using GitHub.

## Architecture

User (VS Code)
     |
     |  SSH (Remote-SSH)
     v
AWS EC2 (Ubuntu)
     |
     |  Python Script
     v
OpenWeather API

## Tech Stack

- AWS EC2 (Ubuntu)
- Python 3
- OpenWeather API
- Git & GitHub
- VS Code Remote-SSH

## EC2 Setup

1. Launch an EC2 instance
   - AMI: Ubuntu 22.04
   - Instance Type: t2.micro
   - Enable SSH (Port 22)

2. Download the `.pem` key and update permissions:
    - chmod 400 openweather.pem(if need)

## Remote SSH Configuration (VS Code)

Edit SSH config file:

Host <EC2_PUBLIC_IP>
    HostName <EC2_PUBLIC_IP>
    User ubuntu
    IdentityFile /path/to/openweather.pem

## Project Setup on EC2 (remote)
cd /home/ubuntu
mkdir openWeather_etl
cd openWeather_etl
touch main.py

## Data Extraction Logic

- Calls OpenWeather API using city name
- Handles API authentication securely
- Converts UNIX timestamps to timezone-aware datetime objects
- Validates HTTP response codes

## Sample Output

- City: Pune
- Temperature: 30°C
- Sunrise Time: 06:15 IST
- Sunset Time: 18:55 IST

## Future Enhancements

- Store raw data in S3 (Bronze layer)
- Add transformation layer (Silver)
- Schedule execution using Airflow
- Load curated data into Redshift







