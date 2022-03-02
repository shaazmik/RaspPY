import RPi.GPIO as GPIO

aux = [22, 23, 27, 18, 15, 14, 3, 2]
leds = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)
GPIO.output(leds,0)
GPIO.cleanup()

while(True):
    for i in range(8):
           GPIO.output(leds[i],GPIO.input(aux[i]))
 
    