import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)   

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)


def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

try:
    while(1):
        
        a = input("Введите число:")
        if a == 'q': 
            break
        elif float(a) % 1 != 0:
            print("Не целое число")
            continue
        elif int(a) > 255:
            print("Превышено число")
            continue
        elif int(a) < 0:
            print("Отрицательное число")
            continue
        
        a = int(a)
        GPIO.output(dac, decimal2binary(a))
        print(a*3.3/255, "Вольт")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
