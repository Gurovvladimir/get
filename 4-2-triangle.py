import RPi.GPIO as GPIO
import time


def decimal2binary(value, bit_depth = 8):
    return [int(x) for x in bin(value)[2:].zfill(bit_depth)]

def binary2decimal(value):
    sum = 0
    for i in range(len(value)):
        sum += value[i]*2**(len(value)-i - 1)
    return sum
dac = [8,11,7,1,0,5,12,6]
Umax = 3.3
bit_depth = len(dac)
frac_amount = 2**bit_depth - 1
T = float(input("Введите период :"))
counter = 0
decriment = 1


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        GPIO.output(dac, decimal2binary(counter, bit_depth=bit_depth))
        time.sleep(T/(2*frac_amount))
        counter += decriment
        if counter == frac_amount:
            decriment = -1
        if counter == 0:
            decriment = 1
except ValueError:
    pass


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup() 
