from machine import Pin
import time

key1 = Pin(38, Pin.IN, Pin.PULL_UP)
prev_state = key1.value()    # prev_state(이전값)에 초기 상태 저장

# 버튼을 꾹 눌러도, 한번 누른 결과에 대해서만 출력
while True:
    current_state = key1.value()   # 0.1초마다 현재 상태 확인
    if current_state != prev_state:   # 버튼을 누르거나 뗀 직후를 감지하면
        prev_state = current_state
        if current_state == 0:        # 버튼을 누르고 있다면
            print("click")
        time.sleep(0.1)