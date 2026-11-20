from machine import Pin
import time
from machine import SoftI2C
from ssd1306 import SSD1306_I2C

# OLED 통신 설정 (sda는 43번 핀, scl은 44번 핀)
# - SDA :: 데이터 핀, 실제 데이터 송수신되는 핀
# - SCL :: 클럭 핀 (통신 신호 맞추는 핀)
i2c = SoftI2C(sda=Pin(43), scl=Pin(44))
# OLED 디스플레이 설정 (128*64)
oled = SSD1306_I2C(128, 64, i2c) 

# (0, 0) 위치에 출력 수행 (가장 상단의 가장 좌측이 (0, 0))
oled.text("hi pyDrone",0,0)    # SDA 핀으로 전달되는 정보
oled.show()