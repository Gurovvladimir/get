import RPi.GPIO as GPIO
import time

leds = [8,11,7,1,0,5,12,6]
aux = [21, 20, 26, 16, 19, 25, 23, 24]

GPIO.setmode(GPIO.BCM)

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)
while True:
    for i in range(0,len(leds)):
        GPIO.output(leds[i],GPIO.input(aux[i]))
