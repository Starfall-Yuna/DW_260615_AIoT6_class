# [ 문제 ]
# nRF Connect 어플로 전달하는 값만큼의 세기로 빨간색 LED 점등하기
# 1023을 넘는 값에 대해서는 1023만큼의 세기만큼 적용

import bluetooth, ble_simple_peripheral
from machine import Pin, PWM

# 블루투스 기능 활성화 + 장치 생성
ble = bluetooth.BLE()
p = ble_simple_peripheral.BLESimplePeripheral(ble, name='pyD_1111')

# Pin.IN :: 지정된 핀을 입력 모드로 설정
# Pin.OUT :: 지정된 핀을 출력 모드로 설정

# duty 초기값 0으로 설정
RED_LED = PWM(Pin(21), freq = 1000, duty=0)

def on_rx(read):    # read :: 수신받은 값(문자열)
    try:
        # 1. 블루투스로 수신받은 값을 정수로 변환
        value = int(read)
        
        # 2. 0 ~ 1023 범위 제한
        if value > 1023:
            value = 1023
        
        # 3. LED 점등
        RED_LED.duty(value)
        print('LED 밝기:', value)
    except ValueError:
        print('잘못된 데이터')

p.on_write(on_rx)