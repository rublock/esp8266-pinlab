import uos, machine
from machine import Pin, PWM

def _init():
    ___pwmpins = [0,2,4,5,12,13,14,15]

    for pin in ___pwmpins:
        machine.PWM(machine.Pin(pin)).deinit()

    ___digitpins = [0,2,4,5,12,13,14,15,16]
    for pin in ___digitpins:
        Pin(pin, Pin.OUT).off()
        Pin(pin, Pin.IN)