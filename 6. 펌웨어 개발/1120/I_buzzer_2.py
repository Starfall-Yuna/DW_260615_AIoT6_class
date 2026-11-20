from machine import Pin, PWM
import time

melody_buzzer = PWM(Pin(6, Pin.OUT), freq=100, duty=0)
melody_buzzer.duty(0)  

# 학교 종소리 노래의 음 높이 값 각각 저장
MELODY = [392, 392, 440, 440, 392, 392, 330, 392, 392,
          330, 330, 293, 0, 392, 392, 440, 440, 392,
          392, 329, 392, 329, 293, 329, 261, 0]

# 각 음의 박자감 넣어주고 싶다면 -> time.sleep() 값도 각각 설정

try:
    while True:
        for note_freq in MELODY:
            # 0.25초간 쉼표 처리 (음이 없음)
            if note_freq == 0:
                melody_buzzer.duty(0)
                time.sleep_ms(250)
            # 지정된 음 재생
            else:
                melody_buzzer.freq(int(note_freq))
                melody_buzzer.duty(7)
                time.sleep_ms(250) 
                melody_buzzer.duty(0)     # 음을 끊어주는 역할
                time.sleep_ms(100) 
except:
    melody_buzzer.duty(0) 
