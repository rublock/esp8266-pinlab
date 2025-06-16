# https://docs.pinlab.ru/products:laboratory_iot:exp14
from machine import Pin
import time
_init()
 
adc = machine.ADC(0) # аналого-цифровой преобразователь АЦП
 
while True:
    value = adc.read()
    print(value) # коэфицент напряжения 0 = 0v, 1023 = 3.3v
    time.sleep(1)
    