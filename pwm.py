# https://docs.pinlab.ru/products:laboratory_iot:exp8
from machine import Pin, PWM
import time
_init()
 
LedPin = 15
 
led = Pin(LedPin, Pin.OUT)
pwmLed = PWM(led) # аппаратный ШИМ
pwmLed.freq(200) # частота в герцах
 
while True:
    pwmLed.duty(150) # коэффициент заполнения 0 = 0%, 1023 = 100%
    time.sleep(1)
    pwmLed.duty(1023)
    time.sleep(1)
    