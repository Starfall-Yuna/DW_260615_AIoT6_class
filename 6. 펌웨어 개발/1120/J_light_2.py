from machine import Pin
from machine import ADC
import time

# 조도센서로 입력받는 중
cds_sensor=ADC(Pin(8))
cds_sensor.atten(ADC.ATTN_11DB)
# LED로 출력하는 중
LED_RED = Pin(21,Pin.OUT)
LED_GREEN = Pin(47,Pin.OUT)
LED_BLUE = Pin(48,Pin.OUT)

while True:
    # 0.5초 간격으로 조도센서 값 조회
    cds_value = cds_sensor.read()
    print(cds_value)
    
    # 조도센서의 값이 500 미만일 때 -> 조명 켜짐
    if cds_value < 500:
        LED_RED.on()
        LED_GREEN.on()
        LED_BLUE.on()
    # 조도센서의 값이 500 이상일 때 -> 조명 꺼짐
    else:
        LED_RED.off()
        LED_GREEN.off()
        LED_BLUE.off()
        
    time.sleep(0.5)
