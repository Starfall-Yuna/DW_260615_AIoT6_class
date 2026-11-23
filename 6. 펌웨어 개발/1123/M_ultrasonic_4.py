import machine
import time
from machine import Pin, PWM

# 기기의 수평이 잘 맞춰져야 측정에 문제X
trigger = Pin(17, mode=Pin.OUT, pull=None)
echo = Pin(1, mode=Pin.IN, pull=None)
trigger.value(0)

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
    while True:    # 0.1초 간격으로 실시간 실행
        distance_cm = get_distance_cm()
        print('장애물과의 거리:', distance_cm)
        
        # 부저음이 들릴 때 출력 속도가 느려진 이유
        #   time.sleep_ms(200) 구문이 원인
        if 2 <= distance_cm < 4:    # 2~4cm 사이라면
            melody_buzzer.freq(261)  # 도
            melody_buzzer.duty(7)
            time.sleep_ms(200) 
        elif 4 <= distance_cm < 6:  # 4~6cm 사이라면
            melody_buzzer.freq(293)  # 레
            melody_buzzer.duty(7)
            time.sleep_ms(200) 
        elif 6 <= distance_cm < 8:  # 6~8cm 사이라면
            melody_buzzer.freq(329)  # 미
            melody_buzzer.duty(7)
            time.sleep_ms(200) 
        elif 8 <= distance_cm < 10:
            melody_buzzer.freq(349)  # 파
            melody_buzzer.duty(7)
            time.sleep_ms(200) 
        elif 10 <= distance_cm < 12:
            melody_buzzer.freq(392)  # 솔
            melody_buzzer.duty(7)
            time.sleep_ms(200) 
        elif 12 <= distance_cm < 14:
            melody_buzzer.freq(440)  # 라
            melody_buzzer.duty(7)
            time.sleep_ms(200) 
        elif 14 <= distance_cm < 16:
            melody_buzzer.freq(493)  # 시
            melody_buzzer.duty(7)
            time.sleep_ms(200) 
        elif 16 <= distance_cm <= 18:
            melody_buzzer.freq(523)  # 높은 도
            melody_buzzer.duty(7)
            time.sleep_ms(200) 
        else:   # 2~18 사이의 값이 아니라면, 
            melody_buzzer.duty(0) 
        
        time.sleep(0.1)
        

except KeyboardInterrupt:
    melody_buzzer.duty(0) 



