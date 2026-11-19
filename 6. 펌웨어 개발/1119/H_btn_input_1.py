from machine import Pin
import time

# 38번 핀을 입력 모드 설정 (풀업 저항)
key1=Pin(39,Pin.IN,Pin.PULL_UP)

# 안 누르면 1, 누르면 0
#    "버튼을 누르면, 흐르던 전류에 막힘 생김"
#    "꾹 누르면 0 값이 계속 출력"
while True:
    print(key1.value())
    time.sleep(0.1)
