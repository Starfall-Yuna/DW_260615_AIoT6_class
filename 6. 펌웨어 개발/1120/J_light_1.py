from machine import Pin
from machine import ADC
import time

# 센서 :: 주변의 환경에 대한 정보를 수치로 표현하는 장치
# 조도센서 값 범위 :: 0 ~ 4095

# 8번 핀 연결 (ADC 입력 모드 설정)
cds_sensor=ADC(Pin(8))
cds_sensor.atten(ADC.ATTN_11DB)   # (큰 값의 입력도 받아낼 수 있게끔) 입력값 보정
#    4000 정도의 밝기를 1000 내외까지 줄여주는 효과 

while True:
    # 조도센서의 값 불러오기 (0.5초 간격)
    cds_value = cds_sensor.read()
    print(cds_value)
    time.sleep(0.5)