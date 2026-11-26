import network
import time

# 존재하는 공유기/핫스팟 이름, 비밀번호
ssid = "DW503"
password = "dwa503**"

# 네트워크 접속 함수
def wifi_connect():
    # STA 모드 설정 + 와이파이 활성화
    wlan = network.WLAN(network.STA_IF) 
    wlan.active(True) 

    # 와이파이 연결이 안 되어있다면,
    if not wlan.isconnected():
        # ssid, 비밀번호로 연결 시도
        print("Connecting to network...")
        wlan.connect(ssid, password)  

        # 300ms 간격, 무한으로 접속 상태 확인
        #   (정상적으로 연결이 안 되면, 무한 반복)
        while not wlan.isconnected():
            time.sleep_ms(300)

        # ifconfig() 확인할 수 있는 값들 ::
        #   IP 구성 (ip주소, 서브넷 마스크, 게이트웨이, DNS)
        
        #  - ip주소 :: 공유기가 드론에 할당해준 주소 (기기 식별 목적)
        #  - 서브넷 마스크 :: 같은 네트워크인지를 판단하는 기준
        #  - 게이트웨이 :: 일반적으로 공유기 주소 (다른 네트워크로 데이터를 전송하기 위한 통로)
        #  - DNS :: 인터넷 사이트 이름을 ip 주소로 바꿔주는 서버 (데이터 전송 목적지 주소 확인)
        #      'google.com' -> [DNS] 8.8.8.8
        print("Connected to network:", wlan.ifconfig())
        return True
    else:
        print("Already connected to network:", wlan.ifconfig())
        return True

if wifi_connect():
    pass
