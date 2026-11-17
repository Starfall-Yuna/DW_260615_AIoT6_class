from machine import Pin
import time

key = Pin(0, Pin.IN, Pin.PULL_UP)
prev_key = key.value()
    # 가장 처음에, 초기 버튼 값에 대해 불러오기 (1, 버튼 안 누름)

try:
    while True:
        curr_key = key.value()     # 실시간으로 현재 버튼값 조회
        if curr_key != prev_key:   # 현재값과 이전값이 다르면, (중복 처리 방지)
            print('이전값:', prev_key)
            print('현재값:', curr_key)
            
            # 이전값을 갱신
            prev_key = curr_key
            print("버튼 눌림",curr_key)
            time.sleep(0.1)
            
            print()

except KeyboardInterrupt:
    print("코드를 종료합니다.")