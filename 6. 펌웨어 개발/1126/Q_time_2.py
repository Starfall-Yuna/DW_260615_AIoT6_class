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

# 인터넷 상 현재 시간(UTC, 국제) 받아옴
#   + 드론의 시간값 갱신 (동기화)
def set_time_from_ntp():
    try:
        ntptime.settime() 
        print("Time synchronized with NTP")
    except Exception as e:
        print("Failed to synchronize time with NTP:", str(e))

# 와이파이 연결 -> 드론 시간 정보 동기화
if wifi_connect():
    set_time_from_ntp() 

while True:
    # 드론의 시간 정보 불러오기
    rtc_time = time.localtime()
    # 날짜 정보와 시간 정보를, 지정된 형식으로 문자열 구성
    #  [0], [1], [2] :: 년도, 월, 일
    #  [3], [4], [5] :: 시, 분, 초
    formatted_time = "{}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(
        rtc_time[0], rtc_time[1], rtc_time[2], rtc_time[3], rtc_time[4], rtc_time[5]
    )
    print("Current Time:", formatted_time)
    time.sleep(1)    # 1초 간격으로 위 내용 수행
