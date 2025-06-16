# https://docs.pinlab.ru/products:laboratory_iot:exp19
from machine import Pin
import time
_init()
 
LedPin = 16
led = Pin(LedPin, Pin.OUT)
 
adc = machine.ADC(0)
 
while True:
    value = adc.read() # читаем значение яркости
    if value > 550:
        led.on()
    else:
        led.off()
    print(value)
    time.sleep(1)
    