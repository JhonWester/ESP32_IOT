from machine import Pin
from utime import sleep

light = Pin(2, Pin.OUT)
light_2 = Pin(15, Pin.OUT)
light_3 = Pin(4, Pin.OUT)

while True:
    light.on()
    sleep(0.5)
    light_2.on()
    light.off()
    sleep(0.5)
    light_2.off()
    light_3.on()
    sleep(0.5)
    light_3.off()
    