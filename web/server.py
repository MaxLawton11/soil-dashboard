DATA_CSV_PATH = "../data.csv"

from flask import Flask, jsonify
import csv

app = Flask(__name__)

def read_data():
    times = []
    resistance = []
    temp = []

    with open(DATA_CSV_PATH) as f:
        reader = csv.DictReader(f)
        for row in reader:
            times.append(row["time"])
            resistance.append(float(row["resistance"]))   # soil moisture
            temp.append(float(row.get("temp", 0)))   # temperature column
    return times, resistance, temp

@app.route("/data")
def data():
    times, resistance, temp = read_data()
    return jsonify({"times": times, "resistance": resistance, "temp": temp})

@app.route("/")
def index():
    return open("index.html").read()

app.run(host="0.0.0.0", port=8000)