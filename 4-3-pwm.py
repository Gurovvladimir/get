import RPi.GPIO as GPIO

GPIO.setwarnings(False)
n = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(n, GPIO.OUT)

p = GPIO.PWM(n, 1000)

p.start(0)

try:
    while(1):
        x = int(input())
        p.ChangeDutyCycle(x)
        print("Volt: ", 3.3*x/100)

finally:
    p.stop()
    GPIO.output(n,0)
    GPIO.cleanup()