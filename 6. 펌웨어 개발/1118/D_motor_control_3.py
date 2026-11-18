# [문제]
# 동작하고자 하는 모터의 번호(1~4)와
# 모터의 세기(1~200)를 입력받고
# 두 입력값을 기반으로 모터를 동작하는 과정을
# 무한 반복하는 코드 작성
# (범위를 벗어난 입력을 받을 시, 프로그램 종료)

from machine import Pin, PWM
import time

M1_motor = PWM(Pin(4), freq = 10000 ,duty=0)
M2_motor = PWM(Pin(5), freq = 10000 ,duty=0)
M3_motor = PWM(Pin(40), freq = 10000 ,duty=0)
M4_motor = PWM(Pin(41), freq = 10000 ,duty=0)

try:
    while True:
        # 1. 입력받기
        num = int(input('모터 번호(1~4 중 하나): '))
        power = int(input('세기(1~200): '))
    
        # 2. 범위를 벗어나면, 프로그램 종료
        if 1>num or num>4 or 1>power or power>200:
            print('잘못된 입력값입니다.')
            break
        
        # 3. 입력값 기반으로, 모터 작동
        if num == 1:
            M1_motor.duty(power)
            time.sleep(3)
            M1_motor.duty(0)
        elif num == 2:
            M2_motor.duty(power)
            time.sleep(3)
            M2_motor.duty(0)
        elif num == 3:
            M3_motor.duty(power)
            time.sleep(3)
            M3_motor.duty(0)
        else:
            M4_motor.duty(power)
            time.sleep(3)
            M4_motor.duty(0)
            
        print('3초간 모터 작동 완료')
    
    
except KeyboardInterrupt:
    print('프로그램을 종료합니다.')