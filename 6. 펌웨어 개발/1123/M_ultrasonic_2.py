import machine
import time
from machine import Pin

trigger = Pin(17, mode=Pin.OUT, pull=None)
echo = Pin(1, mode=Pin.IN, pull=None)
trigger.value(0)

# 함수 :: 초음파센서 활성화 + 신호를 보내서 측정 + 거리값으로 변환
def get_distance_cm():
    trigger.value(0)
    time.sleep_us(5)
    trigger.value(1)
    time.sleep_us(10)
    trigger.value(0)

    pulse_time = machine.time_pulse_us(echo, 1, 30000)
    distance_cm = (pulse_time / 2) / 29.1
    if 2 <= distance_cm <= 200:
        return distance_cm
    else:
        return 0

try:
    while True:
        # 초음파 결과에 따른 거리 값 받아오기
        distance_cm = get_distance_cm()
        if(distance_cm !=0):
            print(distance_cm,"cm")
        time.sleep(0.1)   # 0.1초 간격으로 수행

except KeyboardInterrupt:
    pass

# 초음파 신호가 다시 돌아오는 시간이 길수록
# 장애물과의 거리는 더 멀리 있다.
