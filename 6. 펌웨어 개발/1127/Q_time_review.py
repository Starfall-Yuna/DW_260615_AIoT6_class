# [ 문제 ]
# 인터넷이 되는 공유기에 연결하여 한국 표준 시간을 구하고,
# 시간 정보(시, 분, 초)를 OLED 상에 표시하며
# 아래의 규칙에 맞추어 RGB LED를 작동하는 프로그램을 작성하라
#   - 현재 초 정보가 0이라면, 초록색 LED만 작동
#   - 현재 초 정보가 짝수라면 파란색 LED만 작동
#   - 현재 초 정보가 홀수라면 빨간색 LED만 작동
# OLED 및 RGB LED 출력은 1초 간격으로 수행하라.

import network
import time
import ntptime
import machine
from machine import Pin, PWM
from machine import SoftI2C
from ssd1306 import SSD1306_I2C

# 공유기 이름, 비밀번호
ssid = "DW503"
password = "dwa503**"

# OLED 핀 설정 + 디스플레이 설정
i2c = SoftI2C(sda=Pin(43), scl=Pin(44))
oled = SSD1306_I2C(128, 64, i2c)
# RGB LED 핀 설정
LED_RED = PWM(Pin(21), freq = 1000, duty = 0)
LED_GREEN = PWM(Pin(47), freq = 1000, duty = 0)
LED_BLUE = PWM(Pin(48), freq = 1000, duty = 0)

# 와이파이 연결
def wifi_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        print("Connecting to network...")
        wlan.connect(ssid, password)

        while not wlan.isconnected():
            time.sleep_ms(300)

        print("Connected to network:", wlan.ifconfig())
        return True
    else:
        print("Already connected to network:", wlan.ifconfig())
        return True

# 1. UTC 기준의 서버 시간을 드론에 적용
# 2. 드론의 시간(UTC)을 한국 기준으로 변환
def set_time_from_ntp():
    try:
        ntptime.settime() 
        print("Time synchronized with NTP")
    except Exception as e:
        print("Failed to synchronize time with NTP:", str(e))
def get_kst_time():
    utc_time = time.time()
    kst_time = time.localtime(utc_time + 9 * 3600)  # 9시간 추가
    return kst_time

# 와이파이 연결이 되었다면, UTC 시간 불러오기
if wifi_connect():
    set_time_from_ntp()

while True:
    # 한국 표준 시간으로 변환
    rtc_time = get_kst_time()
    
    # Thonny 상에 출력할 내용
    formatted_time = str(rtc_time[3]) + ':'+ str(rtc_time[4]) + ':' + str(rtc_time[5])
    print('현재 시간은', formatted_time, '입니다.')
    
    # OLED 상에 표현
    hh_mm_ss = "{:02d}:{:02d}:{:02d}".format(rtc_time[3], rtc_time[4], rtc_time[5])
    
    oled.fill(0)
    oled.text(hh_mm_ss, 20, 30)
    oled.show()
    
#   - 현재 초 정보가 0이라면, 초록색 LED만 작동
    if rtc_time[5] == 0:
        LED_RED.duty(0)
        LED_GREEN.duty(500)
        LED_BLUE.duty(0)
#   - 현재 초 정보가 짝수라면 파란색 LED만 작동
    elif rtc_time[5] % 2 == 0:
        LED_RED.duty(0)
        LED_GREEN.duty(0)
        LED_BLUE.duty(500)
#   - 현재 초 정보가 홀수라면 빨간색 LED만 작동
    else:
        LED_RED.duty(500)
        LED_GREEN.duty(0)
        LED_BLUE.duty(0)
    
    time.sleep(1.0)


