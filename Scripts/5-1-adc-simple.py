import RPi.GPIO as GPIO
import time
#
GPIO.setmode(GPIO.BCM)   

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17


GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH) # put 1
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


i = 0
def adc():
    for i in range(256):
        GPIO.output(dac, decimal2binary(i))
        time.sleep(0.001)
        if(GPIO.input(comp) == 0):
            break
    return i

try:
    while(1):
        #a = 1/0
        v = adc()
        volt = v*3.3/256
        print(decimal2binary(v), v, "  ", volt)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
