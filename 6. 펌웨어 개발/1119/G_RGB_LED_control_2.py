from machine import Pin
import time

# 빨간색 등은 21번, 초록색 등은 47번, 파란색 등을 48번
LED_RED = Pin(21,Pin.OUT)
LED_GREEN = Pin(47,Pin.OUT)
LED_BLUE = Pin(48,Pin.OUT)

while True:
    # 빨간색 등 on, 나머지는 off    -> 1초간 유지
    LED_RED.value(1)
    LED_GREEN.value(0)
    LED_BLUE.value(0)
    time.sleep(1.0)
    
    # 초록색 등 on, 나머지는 off    -> 1초간 유지
    LED_RED.value(0)
    LED_GREEN.value(1)
    LED_BLUE.value(0)
    time.sleep(1.0)
    
    # 파란색 등 on, 나머지는 off    -> 1초간 유지
    LED_RED.value(0)
    LED_GREEN.value(0)
    LED_BLUE.value(1)
    time.sleep(1.0)