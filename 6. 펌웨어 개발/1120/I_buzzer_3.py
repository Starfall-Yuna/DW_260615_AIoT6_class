from machine import Pin, PWM
import time

melody_buzzer = PWM(Pin(6, Pin.OUT), freq=100, duty=0)
melody_buzzer.duty(0)

# 버튼1, 버튼2 입력 모드로 핀 연결
key1 = Pin(38, Pin.IN, Pin.PULL_UP)
key2 = Pin(39, Pin.IN, Pin.PULL_UP)

try:
    while True:
        # 버튼을 누르면 0, 버튼을 안 누르면 1
        
        # 버튼1만 눌렀을 때, 도 출력
        if key1.value() == 0 and key2.value() == 1:
            melody_buzzer.duty(7)
            melody_buzzer.freq(261)
        # 버튼2만 눌렀을 때, 레 출력
        elif key1.value() == 1 and key2.value() == 0:
            melody_buzzer.duty(7)
            melody_buzzer.freq(293)
        # 버튼1, 버튼2 모두 눌렀을 때, 미 출력
        elif key1.value() == 0 and key2.value() == 0:
            melody_buzzer.duty(7)
            melody_buzzer.freq(329)
        else:
            melody_buzzer.duty(0)
except:
    melody_buzzer.duty(0) 
