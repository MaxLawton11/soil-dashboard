# sudo chmod +x sample.py 

import csv
from datetime import datetime

from read_moisture import read_moisture
from read_temp import read_ds18b20_fahrenheit

csv_path = "/home/pi/soil-dashboard/data.csv"

timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")

append_row = [timestamp, read_moisture(), read_ds18b20_fahrenheit()]

with open(csv_path, mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(append_row)