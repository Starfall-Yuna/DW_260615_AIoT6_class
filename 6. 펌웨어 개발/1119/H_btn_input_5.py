# [ 문제 ]
# 임의의 변수 값을 변동하고 현재 변수 값을 출력하는 프로그램 작성
# 버튼1을 누르면 :: 누른 횟수만큼 변수값에 1을 증가
# 버튼2를 누르면 :: 누른 횟수만큼 변수값에 1을 감소
# Ctrl+C를 누르면 :: 예외 처리 발생하면서 현재의 변수값을 출력하고 종료

from machine import Pin
import time

key1 = Pin(38, Pin.IN, Pin.PULL_UP)
key2 = Pin(39, Pin.IN, Pin.PULL_UP)
prev_state1 = key1.value()    # 2개 초기값이 모두 1값
prev_state2 = key2.value()

count = 0

def get_key1():    # 버튼1을 누른 순간을 감지 (누른 상태면 1을, 아니라면 0을 반환)
    global prev_state1
    current_state = key1.value() 
    if current_state != prev_state1:
        prev_state1 = current_state
        if current_state == 0:
            return 1
        else:
            return 0
def get_key2():    # 버튼2을 누른 순간을 감지 (누른 상태면 1을, 아니라면 0을 반환)
    global prev_state2
    current_state = key2.value() 
    if current_state != prev_state2:
        prev_state2 = current_state
        if current_state == 0:
            return 1
        else:
            return 0
    
try:
    while True:
        if get_key1():
            count += 1
            print('버튼1 감지: 1 증가합니다.')
            time.sleep(0.1)    # 연산 완료 후, 0.1초 대기
        if get_key2():
            count -= 1
            print('버튼2 감지: 1 감소합니다.')
            time.sleep(0.1)
except KeyboardInterrupt:
    print('최종 count의 값:', count)
    print('프로그램을 종료합니다.')