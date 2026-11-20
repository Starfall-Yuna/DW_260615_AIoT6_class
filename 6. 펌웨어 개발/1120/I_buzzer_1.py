from machine import Pin, PWM
import time

# 6번 핀을 PWM 출력 모드 설정 (주파수 초기값 100으로, 출력 세기 초기값 0으로)
melody_buzzer = PWM(Pin(6, Pin.OUT), freq=100, duty=0)
melody_buzzer.duty(0)  

# 주파수 리스트 (음 높이 값)
frequency_list = [261,293,329,349,392,440,493,523]

try:
    while True:
        # 8개의 주파수 값(음 높이 값)을 하나씩 불러오기
        for frequency in frequency_list:
            # 512 정도 세기로 지정된 음을 내기
            melody_buzzer.duty(10) 
            melody_buzzer.freq(int(frequency))
            time.sleep_ms(500)  
except:
    # 부저를 끄기
    melody_buzzer.duty(0) 