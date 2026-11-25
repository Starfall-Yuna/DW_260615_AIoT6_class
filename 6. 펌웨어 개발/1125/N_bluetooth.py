# [ 문제 ]
# 블루투스를 이용하여 드론과 스마트폰 연결하여 아래와 같이 동작하는 프로그램을 작성하라.
#    (블루투스가 연결된 상태에서만 데이터 전송)
#   - 버튼1을 눌렀을땐, 현재의 조도센서 값을 어플로 출력
#   - 버튼2를 눌렀을땐, 현재의 초음파센서 값을 어플로 출력

import bluetooth, ble_simple_peripheral
import time
import machine
from machine import Pin, ADC

# 블루투스 기능 활성화 + 장치 생성
ble = bluetooth.BLE()
p = ble_simple_peripheral.BLESimplePeripheral(ble, name='pyD_1111')

# 조도센서 핀 설정
cds_sensor=ADC(Pin(8))
cds_sensor.atten(ADC.ATTN_11DB)
# 초음파센서 핀 설정
trigger = Pin(17, mode=Pin.OUT, pull=None)
echo = Pin(1, mode=Pin.IN, pull=None)
trigger.value(0)
# 버튼1, 버튼2 핀 설정
key1 = Pin(38, Pin.IN, Pin.PULL_UP)
key2 = Pin(39, Pin.IN, Pin.PULL_UP)
prev_state1 = key1.value()    # 2개 초기값이 모두 1값
prev_state2 = key2.value()

# 버튼1 입력 감지 (중복 입력 방지)
def get_key1():
    global prev_state1
    current_state = key1.value() 
    if current_state != prev_state1:
        prev_state1 = current_state
        if current_state == 0:
            return 1
        else:
            return 0
# 버튼2 입력 감지 (중복 입력 방지)
def get_key2():
    global prev_state2
    current_state = key2.value() 
    if current_state != prev_state2:
        prev_state2 = current_state
        if current_state == 0:
            return 1
        else:
            return 0
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
        # 블루투스로 외부랑 연결되었다면,
        if p.is_connected():
            # 버튼1 눌렀을 경우,
            if get_key1():
                # 현재의 조도센서 값을 어플로 출력
                light = cds_sensor.read()
                p.send('Light:' + str(light) + '\r\n')
            if get_key2():
                dist = get_distance_cm()
                if dist is None:
                    p.send('Distance : Error!\r\n')
                else:
                    p.send('Distance : ' + str(dist) + '\r\n')
except KeyBoardInterrupt:
    print('프로그램 종료')