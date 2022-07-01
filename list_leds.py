from machine import Pin
from utime import sleep_ms
import _thread 

light_1 = Pin(15, Pin.OUT)
light_2 = Pin(2, Pin.OUT)
light_3 = Pin(4, Pin.OUT)
light_4 = Pin(5, Pin.OUT)
light_5 = Pin(18, Pin.OUT)
light_6 = Pin(19, Pin.OUT)
light_7 = Pin(21, Pin.OUT)
light_8 = Pin(22, Pin.OUT)

leds = [light_1, light_2, light_3, light_4, light_5, light_6, light_7, light_8]

def task():
    
    while True:
    
        for led in leds[:4:1]:
            led.on()
            sleep_ms(500)
            led.off()
            sleep_ms(500)
        
_thread.start_new_thread(task, ())

while True:
      
    for led in leds[4:8:1]:
        led.on()
        sleep_ms(100)
        led.off()
        sleep_ms(100)