import RPi.GPIO as GP
import time

GP.setmode(GP.BCM)

GP.setup(14, GP.OUT)

GP.output(14, 1)

time.sleep(1)

GP.output(14, 0)

time.sleep(1)

GP.output(14, 1)

time.sleep(1)

GP.output(14, 0)

time.sleep(1)

GP.output(14, 1)

time.sleep(1)

GP.output(14, 0)

time.sleep(1)

GP.output(14, 1)

time.sleep(1)

GP.output(14, 0)

time.sleep(1)