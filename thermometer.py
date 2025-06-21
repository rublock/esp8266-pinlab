from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd
import math
import time

_init()

uptime_in_sec = 1

red_led = Pin(16, Pin.OUT)
red_led.off()
 
DEFAULT_I2C_ADDR = 0x27 # Или 0x3F в зависимости от твоей платы IoT
 
adc = machine.ADC(0) # аналого-цифровой преобразователь АЦП

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000) # подготовка шины I2C
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16) # настройка дисплея (2 строки, 16 символов)

Bcoef = 3950
R1 = 10000
Rtnom = 10000
T0 = 273.15

while True:
    value = adc.read()

    """Расчет градусов по цельсию"""
    R2 = (-R1 * value)/(value-1023)
    temp = 1 / (math.log(R2 / Rtnom) / Bcoef + 1/(25+T0)) -T0

    if temp > 24:
        red_led.on()
        lcd.backlight_on() # включение подсветки

    """Расчет времени"""
    hours = uptime_in_sec // 3600
    remaining_seconds = uptime_in_sec % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
 
    print(temp)
    temp = str(temp)

    """Вывод на экран"""
    lcd.putstr("Temp {}\nUptime {}:{}:{}".format(temp, hours, minutes, seconds))
    
    time.sleep(1)
    uptime_in_sec = uptime_in_sec + 1 # счетчик секунд
    lcd.clear()