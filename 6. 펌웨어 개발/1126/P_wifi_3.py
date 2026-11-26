import network
import time

# 존재하는 와이파이 이름, 비밀번호
ssid = "계란마리"
password = "mary135790"

# IP구성 수동 설정값 
static_ip = "192.168.0.150"  # 원하는 고정 IP 주소 설정
subnet_mask = "255.255.255.0" 
gateway = "192.168.0.1" 
dns_server = "8.8.8.8" 

# 와이파이 연결 함수
def wifi_connect():
    # 주변 공유기에 연결할 수 있도록 설정(STA 모드) + 와이파이 기능 활성화
    wlan = network.WLAN(network.STA_IF)  
    wlan.active(True) 

    # 와이파이 연결이 안 되어있다면,
    if not wlan.isconnected():
        print("Connecting to network...")
        # wlan.active(True)
        # 드론 네트워크 기기의 이름 'my-esp32' 설정
        wlan.config(dhcp_hostname="my-esp32")
        # 임의로 지정한 위의 IP 주소를 드론에 적용
        wlan.ifconfig((static_ip, subnet_mask, gateway, dns_server)) 
        wlan.connect(ssid, password)    # 와이파이 연결

        # 300ms 간격으로 접속 상태 확인
        while not wlan.isconnected():
            time.sleep_ms(300)

        print("Connected to network:", wlan.ifconfig())
        return True
    else:
        print("Already connected to network:", wlan.ifconfig())
        return True

if wifi_connect():
    pass

