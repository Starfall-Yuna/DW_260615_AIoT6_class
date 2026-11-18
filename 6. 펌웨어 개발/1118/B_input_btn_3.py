from machine import Pin
import time

key = Pin(0, Pin.IN, Pin.PULL_UP)
    # 0번 핀을 입력 모드로 설정
prev_key = key.value() 

try:
    while True:
        curr_key = key.value()
        if curr_key != prev_key:    # 버튼 상태에 변화가 발생하였을 때
            prev_key = curr_key
            if curr_key == 0:    # 현재 버튼을 누르고 있다면
                print("버튼 눌림",curr_key)
            time.sleep(0.1)      # 0.1초간 유지

except KeyboardInterrupt:
    print("코드를 종료합니다.")