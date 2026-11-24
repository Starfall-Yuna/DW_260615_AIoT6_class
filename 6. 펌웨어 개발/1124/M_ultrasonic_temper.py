# [ 문제 ]
# 온습도센서와 초음파센서를 통해 실시간으로 측정을 수행하고
# 장애물과의 거리 값과 온도값에 있어
# 현재 측정값 및 최대값, 최소값을 실시간으로 Thonny에 출력하는 프로그램 작성
# (실행 간격은 1초 간격)

import machine
import time
import dht
from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C

# 센서 핀 설정
dht11 = dht.DHT11(Pin(18))

trigger = Pin(17, Pin.OUT)
echo = Pin(1, Pin.IN)
trigger.value(0)

# 최고, 최저값 초기화
max_temp = None
min_temp = None
max_dist = None
min_dist = None

# 초음파센서 기반 장애물과의 편도 거리 확인 함수
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
        # 현재 측정값 및 최대값, 최소값을 실시간으로 Thonny에 출력
        
        # 1. 현재 측정값 출력
        dht11.measure()
        temp = dht11.temperature()
        dist = get_distance_cm()
        
        print('현재 온도:', temp)
        print('현재 거리:', dist)
        
        # 2. 온도에 대한 최대, 최소 값 갱신
        if max_temp == None:   # 값이 없다면
            max_temp = temp
        else:    # 숫자값이 있다면
            if max_temp < temp:
                max_temp = temp
        if min_temp == None:
            min_temp = temp
        else:
            if min_temp > temp:
                min_temp = temp
        
        # 3. 거리에 대한 최대, 최소 값 갱신
        if max_dist == None:
            max_dist = dist
        else:
            if max_dist < dist:
                max_dist = dist
        if min_dist == None:
            min_dist = dist
        else:
            if dist != 0 and min_dist > dist:
                min_dist = dist
        
        print('최대 온도:', max_temp)
        print('최소 온도:', min_temp)
        print('최대 거리:', max_dist)
        print('최소 거리:', min_dist)
        print()
        time.sleep(1.0)
except:
    pass