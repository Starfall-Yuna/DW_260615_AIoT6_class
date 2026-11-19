from machine import Pin
import time

# GPIO 21번 핀(빨간색 등)을 출력 모드로 설정
LED_RED = Pin(21,Pin.OUT)

# 빨간색 등에 대해, 1초마다 껐켰
while True:
    LED_RED.value(1)
    time.sleep(1.0)
    LED_RED.value(0)
    time.sleep(1.0)