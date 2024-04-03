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

pwm_pin = 24
dac_pin = 23
frequency = 1000
duty_cycle = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_pin, GPIO.OUT)

pwm = GPIO.PWM(pwm_pin, frequency)
pwm.start(duty_cycle)
try:
    while True:
        duty_cycle = float(input("Введите коэффициент заполнения: "))
        print("Рассчётное напряжение = ", Umax*duty_cycle/100)
        pwm.ChangeDutyCycle(duty_cycle)
        


finally:
    pwm.stop()
    GPIO.cleanup() 
