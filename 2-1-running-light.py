import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [8,11,7,1,0,5,12,6]
#leds = [2, 3, 4, 17, 27, 22, 10, 9]
GPIO.setup(leds, GPIO.OUT)

for i in range(0,3):
    for j in leds:
        GPIO.output(j, 1)
        time.sleep(0.2)
        GPIO.output(j, 0)
GPIO.output(leds, 0)
GPIO.cleanup() 