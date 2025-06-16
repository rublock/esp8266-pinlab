from machine import Pin
import time

"""
_init() - нужен для сброса состояния микроконтроллера в начальное 
состояние, чтобы результаты запуска другого эксперимента не влияли на текущий
"""
_init()
 
LedPin = 2
 
led = Pin(LedPin, Pin.OUT)
 
while True:
    led.off()
    time.sleep(1)
    led.on()
    time.sleep(1)
    