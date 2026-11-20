from machine import Pin
import time
from machine import SoftI2C
from ssd1306 import SSD1306_I2C

i2c = SoftI2C(sda=Pin(43), scl=Pin(44))
oled = SSD1306_I2C(128, 64, i2c)
# 128의 가로, 64의 세로

oled.fill(0)
# (0, 32)에서 127 길이만큼의 가로선(horizonal) 그리기
oled.hline(0, 32, 127, 1)
# (63, 0)에서 63 길이만큼의 세로선(vertical) 그리기
oled.vline(63, 0, 63, 1)
# (0, 0)에서부터 (127, 63)으로 가는 선 그리기
# 좌측 상단에서부터 우측 하단으로
oled.line(0, 0, 127, 63, 1)
# (10, 10)에서 (107, 43) 속이 비어있는 사각형 그리기
oled.rect(10, 10, 107, 43, 1)
# (20, 20)에서 (30, 30) 속이 채워진 사각형 그리기
oled.fill_rect(20, 20, 30, 30, 1)
oled.show()