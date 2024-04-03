import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(el) for el in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

dac = [8,11,7,1,0,5,12,6]

GPIO.setup(dac, GPIO.OUT)
x = 0
a = 1

try:
    while(True):
        try:
            for i in range(8): GPIO.output(dac[i], dec2bin(x)[i])
            time.sleep(1/60)
            if (x == 255): a = -1
            if (x == 0): a = +1
            x = x + a
        except Exception:
            break    
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("END")
