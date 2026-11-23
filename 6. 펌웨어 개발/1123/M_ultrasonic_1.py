import machine
import time
from machine import Pin

# 초음파센서 핀 설정
# "앞에 장애물이 있는가"에 대해 측정
trigger = Pin(17, mode=Pin.OUT, pull=None)    # 출력, 명령어 발신(ESP -> 센서) 핀
echo = Pin(1, mode=Pin.IN, pull=None)         # 입력, 결과값 수신(센서 -> ESP) 핀
trigger.value(0)   # 초음파 신호를 보내기 전 준비

try:
    while True:
        trigger.value(0)   # 초음파 신호를 보내기 전 준비
        time.sleep_us(5)
        trigger.value(1)   # ESP32 -> 초음파센서 :: 명령어 전송
        time.sleep_us(10)
        trigger.value(0)   # 초음파 신호를 보내기 전 준비

        # 초음파센서 결과값 연산 (아래 코드)
        #     :: 초음파신호를 보내고 다시 돌아올 때까지의 소요된 시간 받아옴
        #        (30000 ms만큼 최대한 기다려봄)
        pulse_time = machine.time_pulse_us(echo, 1, 30000)
        # 왕복 시간(ms) -> 편도의 cm 거리로 변환
        distance_cm = (pulse_time / 2) / 29.1
        
        # 2 미만의 값 -> 센서에 오류가 있다고 가정 (교재 상으로)
        if 2 <= distance_cm <= 200:
            print('실제 초음파 결과(왕복 시간):', pulse_time, 'ms')
            print('편도 거리(cm):', distance_cm,"cm")
            print()
        
        # 아래의 작업들을, 0.1초 간격으로 수행
        #   1. 초음파 신호 보내기 전 준비
        #   2. 초음파 센서 활성화
        #   3. 초음파 신호 보내서 돌아오는 시간 측정
        #   4. 왕복시간 -> 편도 거리(cm) 변환
        #   5. 4의 결과를 출력
        time.sleep(0.1)

except KeyboardInterrupt:
    pass
