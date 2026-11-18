from machine import Pin, PWM
import time

# 4개의 모터와 연결된 4번, 5번, 40번 41번 PWM 출력 모드 설정
M1_motor = PWM(Pin(4), freq = 10000 ,duty=0)
M2_motor = PWM(Pin(5), freq = 10000 ,duty=0)
M3_motor = PWM(Pin(40), freq = 10000 ,duty=0)
M4_motor = PWM(Pin(41), freq = 10000 ,duty=0)

try:
    while True:
        # 0의 세기로 3초간 유지
        M1_motor.duty(0)
        M2_motor.duty(0)
        M3_motor.duty(0)
        M4_motor.duty(0)
        print("0")
        time.sleep(3)
        
        # 100의 세기로 1초간 유지
        M1_motor.duty(100)
        M2_motor.duty(100)
        M3_motor.duty(100)
        M4_motor.duty(100)
        print("100")
        time.sleep(1)
        

except KeyboardInterrupt:
    # PWM 출력 모드 해제
    M1_motor.deinit()
    M2_motor.deinit()
    M3_motor.deinit()
    M4_motor.deinit()
    print("코드를 종료합니다.")

