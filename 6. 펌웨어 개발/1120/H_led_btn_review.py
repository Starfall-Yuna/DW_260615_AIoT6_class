# [ 문제 ]
# 버튼1과 버튼2를 조작하여 RGB LED의 파란색 LED의 출력값을 조절하는 프로그램 작성
#    (파란색 LED의 초기 세기는 0으로 설정한다)
# 버튼1을 누르면 :: 파란색 LED의 출력값 세기를 100 증가
#    (1023이 넘으면 에러메시지 출력하며 1023으로 설정)
# 버튼2를 누르면 :: 파란색 LED의 출력값 세기를 100 감소
#    (음수가 되면 에러메시지 출력하며 0으로 설정)
# 각 버튼을 조작할 때마다 현재 LED의 밝기 세기를 출력

from machine import Pin, PWM
import time

# 핀 설정 (파란색 LED, 버튼1, 버튼2)
LED_BLUE = PWM(Pin(48), freq=1000, duty=0)
key1 = Pin(38, Pin.IN, Pin.PULL_UP)
key2 = Pin(39, Pin.IN, Pin.PULL_UP)
prev_state1 = key1.value()
prev_state2 = key2.value()

light = 0

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


try:
    while True:
        # 버튼1 누르면, 밝기 증가
        if get_key1():
            light += 100
            if light > 1023:
                print('Error, 1023으로 설정됩니다.')
                light = 1023
            print('현재 밝기:', light)
            LED_BLUE.duty(light)
        # 버튼2 누르면, 밝기 감소
        if get_key2():
            light -= 100
            if light < 0:
                print('Error, 0으로 설정됩니다.')
                light = 0
            print('현재 밝기:', light)
            LED_BLUE.duty(light)
        
        time.sleep(0.1)   # 0.1초 간격으로 버튼 입력 확인
except KeyboardInterrupt:
    print('최종 LED 밝기:', light)
    print('프로그램을 종료합니다.')