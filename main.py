# https://docs.pinlab.ru/products:laboratory_iot:exp19
from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd
import time
_init()

uptime_in_sec = 1
 
power_led = Pin(1, Pin.OUT)
power_led.off()
red_led = Pin(16, Pin.OUT)

DEFAULT_I2C_ADDR = 0x27 # Или 0x3F в зависимости от твоей платы IoT
 
adc = machine.ADC(0)

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16) # 2 строки, 16 символов

while True:
    value = adc.read() # читаем значение яркости
    if value > 550:
        red_led.on()
        lcd.backlight_on() # включение подсветки
    else:
        red_led.off()
        lcd.backlight_off() # выключение подсветки
    
    value = str(value)
    hours = uptime_in_sec // 3600
    remaining_seconds = uptime_in_sec % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    print(value, hours, minutes, seconds)
    lcd.putstr("Light level {}\nUptime {}:{}:{}".format(value, hours, minutes, seconds))
    time.sleep(1)
    uptime_in_sec = uptime_in_sec + 1
    lcd.clear()
