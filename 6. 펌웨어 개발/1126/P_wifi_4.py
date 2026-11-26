import network
import time

# STA 모드 :: 드론 -> 다른 공유기/와이파이 접속
# AP 모드 ::  다른 기기 -> 드론 접속

# 드론의 와이파이 기기 이름
ap_ssid = "pyDrone1111"    

# 드론의 ap 모드 활성화 함수
def wifi_ap_mode():
    ap = network.WLAN(network.AP_IF)     # AP 기능 설정
    ap.active(True)     # AP 기능 활성화
    ap.config(essid=ap_ssid)     # 드론 와이파이 기기 이름 설정

wifi_ap_mode()  
