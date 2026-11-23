import machine
import time
from machine import Pin, PWM

trigger = Pin(17, mode=Pin.OUT, pull=None)
echo = Pin(1, mode=Pin.IN, pull=None)
trigger.value(0)

# 부저 핀 설정
melody_buzzer = PWM(Pin(6, Pin.OUT), freq=300, duty=0)
melody_buzzer.duty(0)

# 초음파센서 기반 장애물과의 편도 거리 확인 함수
def get_distance_cm():
    trigger.value(0)
    time.sleep_us(5)
    trigger.value(1)
    time.sleep_us(10)
    trigger.value(0)

    pulse_time = machine.time_pulse_us(echo, 1, 30000)
    distance_cm = (pulse_time / 2) / 29.1
    if 2 <= distance_cm <= 200:
        return distance_cm
    else:
        return 0

try:
    while True:     # 0.1초 간격으로 실시간 실행
        # 초음파센서 기반 장애물과의 거리 불러오기
        distance_cm = get_distance_cm()
        
        # 장애물과의 거리가 2~10 사이라면,
        if 2 <= distance_cm <= 10:
            print(distance_cm,"cm")    # 거리 출력
            melody_buzzer.duty(5)
            melody_buzzer.freq(300)
            time.sleep_ms(500)         # 500ms만큼 부저음 울리기
            # 출력된 문장 개수만큼 부저가 울렸음 
        else:
            melody_buzzer.duty(0) 
        
        time.sleep(0.1)
        

except KeyboardInterrupt:
    melody_buzzer.duty(0) 


