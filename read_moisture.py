import RPi.GPIO as GPIO
import time

from read_adc import read_adc

POWER_PIN = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(POWER_PIN, GPIO.OUT)

def read_moisture():
    
    GPIO.output(POWER_PIN, True)  # power probes
    time.sleep(0.05)

    value = read_adc(0)

    GPIO.output(POWER_PIN, False) # turn off

    return value

if __name__=="__main__" :
	print(read_moisture())