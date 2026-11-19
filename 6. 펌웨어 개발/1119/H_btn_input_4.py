from machine import Pin
import time

# 38번, 39번 핀에 입력 모드 설정
# 두 버튼의 초기값(1)에 설정
key1 = Pin(38, Pin.IN, Pin.PULL_UP)
prev_state1 = key1.value()
key2 = Pin(39, Pin.IN, Pin.PULL_UP)
prev_state2 = key2.value()

# 버튼1에 대해 누른 순간을 감지 (중복 입력 방지)
def get_key1():
    global prev_state1
    current_state = key1.value() 
    if current_state != prev_state1:
        prev_state1 = current_state
        if current_state == 0:
            return 1
    else:
        return 0

# 버튼2에 대해 누른 순간을 감지 (중복 입력 방지)
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
    if get_key1():   # get_key1() 결과가 0이라면 (버튼을 눌렀다면)
        print("key1 click")
        time.sleep(0.1)
    
    if get_key2():   # get_key2() 결과가 0이라면 (버튼을 눌렀다면)
        print("key2 click")
        time.sleep(0.1)
