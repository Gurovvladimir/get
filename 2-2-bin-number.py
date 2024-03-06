import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)

dac = [8,11,7,1,0,5,12,6]

number = [random.randint(0,1) for i in dac]

GPIO.setup(dac, GPIO.OUT)

GPIO.output(dac, number)

print(number)
buf = 0
for i in range(0,len(number)):
    buf+= number[i]*2**(7-i)
number = buf
print(number)

time.sleep(10)

mas = [2,255,127,64,32,5,0, 0]
mas_duplicate = mas
mas_2=[[],[],[],[],[],[],[],[]]
for i in range(0,8):
    for j in range(0,8):
        mas_2[i].append(mas_duplicate[i]//2**(7-j))
        mas_duplicate[i] -= (mas_duplicate[i] // 2**(7-j)) * 2**(7-j)  
print(mas_2)

for i in range(0,8):
    GPIO.output(dac, mas_2[i])
    time.sleep(0.2)
mas_result = [73.9,3.258*1000*1000,1.675*1000*1000,0.868*1000*1000,0.457*1000*1000,112.3,48.1]
print(mas_result)
GPIO.output(dac, 0)
GPIO.cleanup() 
