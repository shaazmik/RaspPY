import RPi.GPIO as GPIO
import time
#
GPIO.setmode(GPIO.BCM)   

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
array = [0, 0, 0, 0, 0, 0, 0, 0]
dac_reverse   = [10, 9, 11, 5, 6, 13, 19, 26]
leds = [24, 25, 8, 7, 12, 16, 20, 21]

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH) # put 1
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


i = 0
def adc():  
    for i in 7, 6, 5, 4, 3, 2, 1, 0:
        GPIO.output(dac_reverse[i], 1)
        array[7 - i] = 1
        time.sleep(0.007)
        if(GPIO.input(comp) == 0):
            GPIO.output(dac_reverse[i], 0)
            array[7-i] = 0
    return
            
try:
    while(1):
        v = 0
        array = [0, 0, 0, 0, 0, 0, 0, 0]
        GPIO.output(dac, array)
        adc()
        for j in range(8):
            v += array[j]*(2**(7-j))
            volt = v*3.3/256
        print(decimal2binary(v), v, "  ", volt)
        GPIO.output(leds, 0)
        k = 0
        for k in range(9):
            if(v < k * 32 + 5):
                j = 0
                for j in range(k):
                    GPIO.output(leds[j], 1)
                    #print(j)
                break    
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
