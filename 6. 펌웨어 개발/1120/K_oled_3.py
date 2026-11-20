from machine import Pin
import time
from machine import SoftI2C
from ssd1306 import SSD1306_I2C

i2c = SoftI2C(sda=Pin(43), scl=Pin(44))
oled = SSD1306_I2C(128, 64, i2c)

# 임의의 변수 0 값으로 설정
cnt = 0

try:
    while True:
        oled.fill(0)    # 화면 비우기 (안해주면, 출력값들이 겹쳐짐)
        oled.text(str(cnt),50,20)   # 현재 cnt값을 (50, 20) 위치 출력
        oled.show()     # 화면 보여주기
        
        cnt += 1
        time.sleep(0.2)    # 0.2초 간격 실행
except:
    # oled.fill(0)
    # oled.show()
    pass   # 프로그램 종료