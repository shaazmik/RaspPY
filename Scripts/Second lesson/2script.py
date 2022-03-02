import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BCM)

dac = [10, 9, 11, 5, 6, 13, 19, 26]

GPIO.setup(dac, GPIO.OUT)

number = int(input())

for i in range(8):
    flag = (number // (1<<i)) % 2
    print("DEB: " + str(i) + " " + str(flag))
    GPIO.output(dac[i], flag)
    
time.sleep(10)

GPIO.output(dac, 0)
GPIO.cleanup()
    
