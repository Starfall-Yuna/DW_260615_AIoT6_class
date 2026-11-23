# [ 문제 ]
# 온습도센서와 초음파센서를 실시간으로 적절히 활용하여 아래와 같이 기능하는 프로그램을 작성하라.
#  - 온도, 습도, 장애물과의 거리에 대한 값은 Thonny의 콘솔에 실시간 출력
#  - 온도 및 습도에 따라 쾌적도를 OLED 상단에 출력
#      1. 온도가 20 ~ 26 사이이며 습도가 40 ~ 60 사이라면, 'Comfort' 출력
#      2. 온도가 30 이상이거나 습도가 70 이상이라면, 'Warning' 출력
#      3. 그 이외에 해당한다면, 'Normal' 출력
#  - 초음파센서 값이 5 이하라면, 아래의 양식대로 OLED 하단에 출력
#      'Dist: (초음파센서_값) cm
#      'Danger!'

import machine
import time
import dht
from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C

# 온습도센서, 초음파센서, OLED 설정
dht11 = dht.DHT11(Pin(18))

trigger = Pin(17, Pin.OUT)
echo = Pin(1, Pin.IN)
trigger.value(0)

i2c = SoftI2C(sda=Pin(43), scl=Pin(44))
oled = SSD1306_I2C(128, 64, i2c)

# 초음파센서 기반 장애물과의 편도 거리 확인 함수
def get_distance_cm():
    trigger.value(0)
    time.sleep_us(5)
    trigger.value(1)
    time.sleep_us(10)
    trigger.value(0)

    pulse_time = machine.time_pulse_us(echo, 1, 30000)
    distance_cm = (pulse_time / 2) / 29.1
    if 2 <= distance_cm <= 200:
        return distance_cm
    else:
        return 0

try:
    while True:
        # 온도, 습도, 장애물과의 거리에 대한 값은 Thonny 실시간 출력
        dht11.measure()
        temp = dht11.temperature()
        humi = dht11.humidity()
        dis_cm = get_distance_cm()
        
        print('온도:', temp, 'C')
        print('습도:', humi, '%')
        print('장애물과의 거리', dis_cm, 'cm')
        
        # OLED 상의 화면 비우기
        oled.fill(0)
        
        # 온도 및 습도에 따라 쾌적도를 OLED 상단에 출력
        if 20<=temp<=26 and 40<=humi<=60:
            oled.text('Comfort', 30, 10)
        elif temp>=30 or humi>=70:
            oled.text('Warning', 30, 10)
        else:
            oled.text('Normal', 30, 10)
        
        # 초음파센서 값이 5 이하라면, OLED 상에 에러메시지 출력
        if dis_cm <= 5:
            oled.text('DIST: '+str(round(dis_cm, 1))+'cm', 30, 30)
            oled.text('DANGER!', 30, 50)
        
        oled.show()
        time.sleep(0.5)
        print()
            
except:
    oled.fill(0)
    oled.show()
