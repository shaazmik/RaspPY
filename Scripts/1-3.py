import RPi.GPIO as GP

GP.setmode(GP.BCM)

GP.setup(14, GP.OUT)
GP.setup(15, GP.IN)

while True:
    GP.output(14, GP.input(15))