# 2-1.LED제어하기_1.py
# 42번 핀의 초록등 2초씩 점멸(점등-소등) 무한 반복

from machine import Pin
import time

green_led = Pin(42,Pin.OUT)
    # 42번 핀(초록등)을 출력 모드로 설정

while True:
    green_led.value(1)    # 출력값을 1로 설정 (점등)
    time.sleep(2.0)       # 2초간 유지
    green_led.value(0)    # 출력값을 0으로 설정 (소등)
    time.sleep(2.0)
    