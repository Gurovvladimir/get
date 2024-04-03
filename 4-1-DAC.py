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
frac_amount = 2**bit_depth 

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        number = input("Введите число от 0 до 255: ")
        number = int(number)
        if number > 255: 
            print("inserted value overflow")
        elif number < 0:
            print("inserted negative value")
        print ("Предполагаемое напряжение =", round(Umax*number/frac_amount, 2), "B")
        GPIO.output(dac, decimal2binary(number, bit_depth=bit_depth))
except ValueError:
    if number ==  "q": pass
    elif "." in number:
        print("float inserted")
    else:
        print("srting inserted")
    
        


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup() 
