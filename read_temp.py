import RPi.GPIO as GPIO
import os
import glob
import time

# GPIO pins
POWER_PIN = 13  # GPIO that powers the DS18B20
DATA_PIN = 6    # 1-Wire data pin

# Setup GPIO (do this once in your program)
GPIO.setmode(GPIO.BCM)
GPIO.setup(POWER_PIN, GPIO.OUT)

# Initialize 1-Wire (do this once in your program)
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

# Find the sensor folder
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_ds18b20_fahrenheit():
    """
    Powers on the DS18B20, reads the temperature in Fahrenheit, and powers it off.
    Returns:
        float: temperature in °F
    """
    # Power on
    GPIO.output(POWER_PIN, GPIO.HIGH)
    time.sleep(0.5)  # wait for sensor to stabilize

    # Read raw temperature
    with open(device_file, 'r') as f:
        lines = f.readlines()

    # Wait until sensor is ready
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        with open(device_file, 'r') as f:
            lines = f.readlines()

    # Parse temperature in Celsius
    temp_c = float(lines[1].split('t=')[-1]) / 1000.0
    temp_f = (temp_c * 9/5) + 32

    # Power off
    GPIO.output(POWER_PIN, GPIO.LOW)

    return temp_f

# Example usage:
if __name__ == "__main__":
    temp = read_ds18b20_fahrenheit()
    print(f"Temperature: {temp:.2f} °F")