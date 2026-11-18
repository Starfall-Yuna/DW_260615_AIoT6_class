# [문제]
# Key 버튼을 1번 누를 때마다, 버튼을 누른 총 횟수를 출력하고
# Key 버튼을 총 5번 눌렀을 때 실행을 종료하는 프로그램 작성

# 틀린 코드...

from machine import Pin
import time

key = Pin(0, Pin.IN, Pin.PULL_UP)

count = 0
while True:
    curr_key = key.value()
    
    # 버튼을 꾹 누르고 있으면...
    # 1번 누른걸로 취급되지 못하고, 여러번 누른걸로 취급해버림
    if curr_key == 0:
        count += 1
        print(count, '번째로 버튼 입력함')
    if count == 5:
        print('시스템을 종료합니다.')
        break;
    
    time.sleep(0.1)
        # 0.1초마다 버튼의 현재값 확인 (1초동안만 꾹 눌러도 10번 누른걸로 취급)
