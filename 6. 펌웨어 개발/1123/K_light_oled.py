# [ 문제 ]
# 조도센서의 값에 따라 OLED 출력값을 아래의 규칙대로 바꾸어라.
#  - 좌측 상단에는 실시간으로 측정되는 조도센서의 값을 출력
#  - 조도센서의 값이 1000 이상이라면, 화면의 정중앙(30, 35)에 "Bright"를 출력
#  - 조도센서의 값이 400 이상 1000 미만이라면, 화면의 정중앙(30, 35)에 "Normal"을 출력
#  - 조도센서의 값이 400 미만이라면, 화면의 정중앙(40, 35)에 "Dark"를 출력
# 프로그램 종료 시, OLED 화면을 비울 것

from machine import Pin, PWM, ADC, SoftI2C
from ssd1306 import SSD1306_I2C
import time

# 조도센서 핀 설정
cds = ADC(Pin(8))
cds.atten(ADC.ATTN_11DB)
# OLED 핀 설정
i2c = SoftI2C(sda=Pin(43), scl=Pin(44))
oled = SSD1306_I2C(128, 64, i2c)

try:
    while True:
        # 좌측 상단(0, 0)에는 실시간으로 측정되는 조도센서의 값을 출력
        light = cds.read()
        print('현재 밝기:', light)    # Thonny 상의 출력
        
        oled.fill(0)
        oled.text('LIGHT:' + str(light), 0, 0)
        
        # 조도센서 값에 따라서, 밝기 상태 출력
        if light >= 1000:
            oled.text('BRIGHT', 30, 35)
        elif light < 1000 and light >= 400:
            oled.text('NORMAL', 30, 35)
        else:
            oled.text('DARK', 40, 35)
        
        # 실질적인 출력 수행
        oled.show()
        time.sleep(0.5)
except:
    # - 프로그램 종료 시, OLED 화면을 비울 것
    oled.fill(0)
    oled.show()

