from machine import Pin,ADC
import time

adc = ADC(Pin(2))
    # 2번 핀을 ADC(전압, 0 ~ 4095 범위) 입력 설정

# 배터리 연결X :: 불규칙적으로 값 확인
# 배터리 연결O :: 비교적 규칙적으로 값 확인

try:
    while True:
        adc_value = adc.read()     # 전압값 확인 및 저장
        
        print(adc_value)

        time.sleep(1.0)      # 1초마다 값 확인

except KeyboardInterrupt:
    print("코드를 종료합니다.")