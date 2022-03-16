import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)   

pin = 22

GPIO.setup(pin, GPIO.OUT)

p = GPIO.PWM(pin, 1000)  
p.start(1)
#p.start(dc)

try:
    while(1):
        a = float(input("koef: "))
        if a == 0:
            a = 1
        p.start(a) ##duty cycle
        
        if input("Press q to stop: ") == 'q':
            p.stop()
            break
finally:
    GPIO.output(pin, 0)
    GPIO.cleanup()