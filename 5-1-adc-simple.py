import RPi.GPIO as GPIO
import time


dac = [8,11,7,1,0,5,12,6]
comp = 0
troyka = 0

Umax = 3.3
bit_depth = len(dac)
frac_amount = 2**bit_depth

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value, bit_depth = 8):
    return [int(x) for x in bin(value)[2:].zfill(bit_depth)]

def adc(dac = dac):
    for x in range(frac_amount):
        signal_out = decimal2binary(x)
        GPIO.output(dac, signal_out)
        time.sleep(0.001)
        if GPIO.input(comp) == 0:
            voltage = Umax * x / frac_amount
            print("ADC value = {}, signal = {}, voltage = {}".format(x, signal_out,voltage))


try:
    while True:
        adc()





finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka,0)
    GPIO.cleanup()