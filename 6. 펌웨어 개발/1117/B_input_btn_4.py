# [문제]
# Key 버튼을 1번 누를 때마다, 버튼을 누른 총 횟수를 출력하고
# Key 버튼을 총 5번 눌렀을 때 실행을 종료하는 프로그램 작성

from machine import Pin
import time

key = Pin(0, Pin.IN, Pin.PULL_UP)

prev_key = key.value()  # 버튼의 이전 상태 저장
count = 0

try:
    while True:
        curr_key = key.value()

        # 해당 조건문으로, 버튼 입력에 대한 중복 처리 방지
        if curr_key != prev_key:
            prev_key = curr_key

            if curr_key == 0:
                count += 1
                print('버튼 누른 횟수:', count)

            if count == 5:
                print('프로그램을 종료합니다')
                    break

            time.sleep(0.1)

except KeyboardInterrupt:
    print("코드를 종료합니다.")