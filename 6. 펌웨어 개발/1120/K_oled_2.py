from machine import Pin
import time
from machine import SoftI2C
from ssd1306 import SSD1306_I2C

i2c = SoftI2C(sda=Pin(43), scl=Pin(44))
oled = SSD1306_I2C(128, 64, i2c)

# (0, 0) :: 가장 좌측의 가장 상단
# (20, 30) ::
#    가장 좌측으로부터 20 정도 떨어지고 (가로)
#    가장 상단으로부터 30 정도 떨어진 곳에 (세로)
#    출력을 수행
oled.text("hi pyDrone",20,30) 
oled.show()    # 여기에서, 최종적인 출력이 수행

