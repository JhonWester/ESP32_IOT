from machine import Pin
from utime import sleep_ms

red = Pin(15, Pin.OUT)
green = Pin(2, Pin.OUT)
blue = Pin(4, Pin.OUT)

def display(A, B, C):
  red.value(A)
  green.value(B)
  blue.value(C)

while True:
  display(0, 0, 0)
  sleep_ms(300)
  display(0, 0, 1)
  sleep_ms(300)
  display(0, 1, 0)
  sleep_ms(300)
  display(0, 1, 1)
  sleep_ms(300)
  display(1, 0, 0)
  sleep_ms(300)
  display(1, 0, 1)
  sleep_ms(300)
  display(1, 1, 0)
  sleep_ms(300)
  display(1, 1, 1)
  sleep_ms(300)
