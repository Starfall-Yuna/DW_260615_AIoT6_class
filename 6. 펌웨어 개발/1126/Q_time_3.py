import network
import time
import ntptime

# 공유기 이름, 비밀번호
ssid = "DW503"
password = "dwa503**"

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

# UTC 기준 시간 정보 불러오기 + 드론에 적용
def set_time_from_ntp():
    try:
        ntptime.settime() 
        print("Time synchronized with NTP")
    except Exception as e:
        print("Failed to synchronize time with NTP:", str(e))

# 한국 표준 시간으로 변환 (UTC 시간 + 9시간)
def get_kst_time():
    utc_time = time.time()
    kst_time = time.localtime(utc_time + 9 * 3600)  # 9시간 추가
    return kst_time

# 와이파이 연결 -> 드론 시간 동기화
if wifi_connect():
    set_time_from_ntp() 

while True:
    # 드론 시간(UTC)을 한국 시간으로 변환
    rtc_time = get_kst_time()
    # 날짜 정보, 시간 정보 형식에 맞추고, 출력 진행
    formatted_time = "{}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(
        rtc_time[0], rtc_time[1], rtc_time[2], rtc_time[3], rtc_time[4], rtc_time[5]
    )
    print("Current Time (KST):", formatted_time)
    time.sleep(1)
