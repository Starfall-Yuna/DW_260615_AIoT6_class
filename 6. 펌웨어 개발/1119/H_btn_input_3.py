from machine import Pin
import time

key1 = Pin(38, Pin.IN, Pin.PULL_UP)
prev_state = key1.value()    # 1 값으로 시작

# 버튼 한번 누른 내용에 대해서만 출력 수행
def get_key1():
    global prev_state    # 전역 변수 - 지역 변수
    current_state = key1.value()     # 현재값 체크 (0.1초마다 체크)
    if current_state != prev_state:  # 버튼을 누른 직후이거나 버튼을 뗀 직후라면
        prev_state = current_state
        if current_state == 0:       # 현재 버튼을 눌렀다면, 1 반환
            return 1
        else:
            return 0

while True:
    if get_key1():    # get_key1() 실행 (0.1초 단위로 실행)
        # 1의 값으로 반환받으면 if가 true, 아래의 구문이 실행
        print("click")
        time.sleep(0.1)