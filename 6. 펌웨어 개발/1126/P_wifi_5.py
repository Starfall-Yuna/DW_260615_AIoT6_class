# [ 문제 ]
# 버튼1 및 버튼2를 누를 때, 아래와 같이 동작하는 프로그램을 작성하라.
# 버튼1을 눌렀을 때,
#   STA 모드가 활성화 상태라면, 비활성화 상태로 전환
#   STA 모드가 비활성화 상태라면, 활성화 상태로 전환하고 지정된 와이파이로 접속 시도
#      (10초 내외로 접속되지 않는다면, '접속 실패' 출력한 뒤 STA 모드 비활성화로 전환)
# 버튼2를 눌렀을 때,
#   AP 모드가 활성화 상태라면, 비활성화 상태로 전환
#   AP 모드가 비활성화 상태라면, 활성화 상태로 전환

import network
import time
from machine import Pin

# 버튼1, 버튼2 핀 설정
key1 = Pin(38, Pin.IN, Pin.PULL_UP)
key2 = Pin(39, Pin.IN, Pin.PULL_UP)
prev_state1 = key1.value()
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

# 연결할 와이파이 정보
ssid = "DW503"
password = "dwa503**"

# STA 모드의 와이파이 설정
sta = network.WLAN(network.STA_IF)  
sta.active(False) 
# AP 모드의 와이파이 설정
ap = network.WLAN(network.AP_IF)     # AP 기능 설정
ap.active(False)

# STA 모드 :: 드론 -> 다른 공유기/핫스팟/네트워크 접속
# AP 모드 :: 다른 기기 -> 드론 접속

while True:
    # 버튼1을 눌렀을 때, STA 모드 활성화/비활성화 (sta 활용)
    if get_key1():
        # STA 활성화되어 있다면,
        if sta.active():
            sta.active(False)
            print('STA Off')
        # STA 비활성화되어 있다면, 
        else:
            sta.active(True)
            print('STA On')
            
            sta.connect(ssid, password)
            print('Connecting to WiFi...')
            
            # 0.3초 간격으로 최대 30번 연결 상태 확인 (약 9초)
            for i in range(30):
                # 시간 내로 연결이 되면, 루프 탈출
                if sta.isconnected():
                    break
                time.sleep_ms(300)
            
            if sta.isconnected():
                print('Wifi Connected')
            else:
                print('접속 실패')
                sta.active(False)
            
    # 버튼2를 눌렀을 때, AP 모드 활성화/비활성화 (ap 활용)
    if get_key2():
        # AP 활성화되어 있다면,
        if ap.active():
            ap.active(False)
            print('AP Off')
        # AP 비활성화되어 있다면,  
        else:
            ap.active(True)
            ap.config(essid = '파이드론')
            print('AP On')
        
    
    
    