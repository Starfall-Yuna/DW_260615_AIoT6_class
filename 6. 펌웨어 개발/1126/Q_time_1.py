import network
import time
import ntptime 

# 실제 인터넷이 되는 공유기 이름, 비밀번호
ssid = "DW503"
password = "dwa503**"

# 지정된 공유기로 와이파이 연결
def wifi_connect():
    # STA 모드 설정 + 활성화
    wlan = network.WLAN(network.STA_IF) 
    wlan.active(True) 

    # 연결된게 없으면, 와이파이 연결 시도
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

# 와이파이가 연결되었다면,
if wifi_connect():
    set_time_from_ntp() 
    print(time.localtime())    # 드론의 시간 정보 불러오기
    # (년도, 월, 일, 시, 분, 초, 요일, 한 해 중 몇번째 날)
    
    
    
    