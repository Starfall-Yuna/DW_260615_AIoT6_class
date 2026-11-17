# [문제]
# 42번 핀의 초록등 점멸(점등-소등) 무한 반복하는 코드
#    점등하는 시간과 소등하는 시간은 입력값으로 설정
#    점등, 소등이 일어날 때마다, 몇번째 점등/소등인지 출력하게끔 설정
#    Ctrl+C 입력 또는 정지 시, 소등하며 프로그램 종료

from machine import Pin
import time

green_led = Pin(42,Pin.OUT)

on = int(input('점등할 시간을 입력하세요.'))
off = int(input('소등할 시간을 입력하세요.'))

count = 0
try:
    while True:
        count += 1
        
        print(count, '번째 점등입니다.')
        green_led.on()
        time.sleep(on)
        
        print(count, '번째 소등입니다.')
        green_led.off()
        time.sleep(off)

except KeyboardInterrupt:
    green_led.off()
    print("코드를 종료합니다.")

