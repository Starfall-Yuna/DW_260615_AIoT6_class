from machine import Pin, PWM
import time

# 배터리 필요한 코드 (프로펠러가 세게 돌아가요)

# 4번 핀에 PWM 출력 핀으로 설정 (출력값의 정도 조절 가능)
#    - freq :: 주파수값 설정 (매끄럽게 작동하기 위한 설정값)
#    - duty :: 초기의 전력 세기를 0으로 설정 (0 ~ 1023)
M1_motor = PWM(Pin(4), freq = 10000 ,duty=0)

try:
    while True:
        M1_motor.duty(0)
        print("0")
        time.sleep(2)     # 0의 세기를 2초간 지속
        
        M1_motor.duty(100)
        print("100")
        time.sleep(1)     # 100의 세기를 1초간 지속
        
        M1_motor.duty(200)
        print("200")
        time.sleep(2)     # 200의 세기를 2초간 지속

except KeyboardInterrupt:
    M1_motor.deinit()
    print("코드를 종료합니다.")
