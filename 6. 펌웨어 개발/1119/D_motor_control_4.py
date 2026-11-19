# [문제]
#  1번 모터 -> 2번 모터 -> 3번 모터 -> 4번 모터 -> 1번 ... 순으로
#  모터를 100 정도 세기만큼 3초동안 작동시키는 코드 무한 반복

from machine import Pin, PWM
import time

M1_motor = PWM(Pin(4), freq = 10000 ,duty=0)
M2_motor = PWM(Pin(5), freq = 10000 ,duty=0)
M3_motor = PWM(Pin(40), freq = 10000 ,duty=0)
M4_motor = PWM(Pin(41), freq = 10000 ,duty=0)

try:
    while True:
        # duty 통해서 출력값의 세기 조정
        M1_motor.duty(100)
        time.sleep(3.0)
        M1_motor.duty(0)
        
        M2_motor.duty(100)
        time.sleep(3.0)
        M2_motor.duty(0)
        
        M3_motor.duty(100)
        time.sleep(3.0)
        M3_motor.duty(0)
        
        M4_motor.duty(100)
        time.sleep(3.0)
        M4_motor.duty(0)
        
except KeyboardInterrupt:
    print('프로그램을 종료합니다.')