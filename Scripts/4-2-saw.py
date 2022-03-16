import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)


def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

try:
    period = 3; ##seconds 
    time_tap = period / 510
    while(1):
        a = 0
        while(a < 255):
            GPIO.output(dac, decimal2binary(a))
            a+= 1
            time.sleep(time_tap)
        while(a > 0):
            GPIO.output(dac, decimal2binary(a))
            a-= 1
            time.sleep(time_tap)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()