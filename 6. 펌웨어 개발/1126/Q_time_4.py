import network
import time
import ntptime
from machine import Pin
from machine import SoftI2C
from ssd1306 import SSD1306_I2C

# 공유기 이름, 비밀번호
ssid = "DW503"
password = "dwa503**"

# OLED 핀 설정 + 디스플레이 설정
i2c = SoftI2C(sda=Pin(43), scl=Pin(44))
oled = SSD1306_I2C(128, 64, i2c)

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

# 와이파이 연결 -> UTC 시간 불러오기
if wifi_connect():
    set_time_from_ntp() 

while True:
    # 드론의 시간을 한국 기준으로 변환
    rtc_time = get_kst_time()
    formatted_time = "{}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(
        rtc_time[0], rtc_time[1], rtc_time[2], rtc_time[3], rtc_time[4], rtc_time[5]
    )
    print("Current Time (KST):", formatted_time)
    
    yyyy_mm_dd = "{}-{:02d}-{:02d}".format(rtc_time[0], rtc_time[1], rtc_time[2])
    hh_mm_ss = "{:02d}:{:02d}:{:02d}".format(rtc_time[3], rtc_time[4], rtc_time[5])

    # 화면을 비워주기
    oled.fill(0)
    # 날짜 표현
    oled.text(yyyy_mm_dd, 20, 20)
    # 시간 표현
    oled.text(hh_mm_ss, 20, 30)
    # 요일 표현
    week_idx = rtc_time[6]
    if week_idx == 0:   oled.text('MON', 20, 40)
    elif week_idx == 1: oled.text('TUE', 20, 40)
    elif week_idx == 2: oled.text('WED', 20, 40)
    elif week_idx == 3: oled.text('THU', 20, 40)
    elif week_idx == 4: oled.text('FRI', 20, 40)
    elif week_idx == 5: oled.text('SAT', 20, 40)
    else: oled.text('SUN', 20, 40)
    # 한 해 중 몇번째 날인지 표현
    oled.text(str(rtc_time[7]) + ' of 365', 20, 50)
    
    oled.show()   # 실질적으로 화면에 표시
    
    time.sleep(1)
    
    
    