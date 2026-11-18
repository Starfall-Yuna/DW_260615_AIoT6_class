# [문제]
# 42번 핀의 초록등 점멸(점등-소등) 무한 반복하는 코드
#    점등하는 시간과 소등하는 시간은 입력값으로 설정
#    점등, 소등이 일어날 때마다, 몇번째 점등/소등인지 출력하게끔 설정
#    Ctrl+C 입력 또는 정지 시, 소등하며 프로그램 종료

from machine import Pin
import time

green_led = Pin(42,Pin.OUT)

# 점등, 소등을 지속할 시간 입력받기 (int로 받기)
on = int(input('점등할 시간을 입력하세요.'))
off = int(input('소등할 시간을 입력하세요.'))

count = 0     # 몇번째 점등/소등인지를 카운팅할 변수 생성
try:
    while True:
        count += 1   # 점멸 한 세트당 1씩 증가
        
        print(count, '번째 점등입니다.')
        green_led.on()
        time.sleep(on)     # 입력값만큼 점등 지속
        
        print(count, '번째 소등입니다.')
        green_led.off()
        time.sleep(off)    # 입력값만큼 소등 지속

except KeyboardInterrupt:
    green_led.off()
    print("코드를 종료합니다.")

