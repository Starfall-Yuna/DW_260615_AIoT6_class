# 42번 핀의 초록등 2초씩 점등-소등 무한 반복

from machine import Pin
import time

green_led = Pin(42,Pin.OUT)

while True:
    green_led.value(1)
    time.sleep(2.0)
    green_led.value(0)
    time.sleep(2.0)
    