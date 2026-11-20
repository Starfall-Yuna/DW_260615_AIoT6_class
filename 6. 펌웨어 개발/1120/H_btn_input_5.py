from machine import Pin
import time

key1 = Pin(38, Pin.IN, Pin.PULL_UP)
prev_state1 = key1.value()
key2 = Pin(39, Pin.IN, Pin.PULL_UP)
prev_state2 = key2.value()

LED_RED = Pin(21,Pin.OUT)
LED_GREEN = Pin(47,Pin.OUT)
LED_BLUE = Pin(48,Pin.OUT)

state = 0

# 초기값(state = 0) :: 빨간색 불이 들어옴
LED_RED.value(1)
LED_GREEN.value(0)
LED_BLUE.value(0)

def get_key1():
    global prev_state1
    current_state = key1.value() 
    if current_state != prev_state1:
        prev_state1 = current_state
        if current_state == 0:
            return 1
    else:
        return 0

def get_key2():
    global prev_state2
    current_state = key2.value() 
    if current_state != prev_state2:
        prev_state2 = current_state
        if current_state == 0:
            return 1
    else:
        return 0

while True:
    # 버튼1을 누르면 :: state값 감소 (파랑(2) -> 초록(1) -> 빨강(0))
    if get_key1():
        if state > 0:
            state = state - 1
        print(state)
        time.sleep(0.1)
        
    # 버튼2를 누르면 :: state값 증가 (빨강(0) -> 초록(1) -> 파랑(2))
    if get_key2():
        if state < 2:
            state = state + 1
        print(state)
        time.sleep(0.1)
    
    if state == 0:   # state=0 :: 빨강
        LED_RED.value(1)
        LED_GREEN.value(0)
        LED_BLUE.value(0)
    elif state == 1: # state=1 :: 초록
        LED_RED.value(0)
        LED_GREEN.value(1)
        LED_BLUE.value(0)
    elif state == 2: # state=2 :: 파랑
        LED_RED.value(0)
        LED_GREEN.value(0)
        LED_BLUE.value(1)