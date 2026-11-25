print("Scanning for WiFi networks, please wait...")
print("")

# 와이파이 연결 전, 주변에 있는 와이파이 탐색

# 와이파이 통신에 활용
import network
# STA 모드(드론이 공유기 연결O 모드) 설정 + 와이파이 기능 활성화
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

# 네트워크 인증/보안 방식 나열 (Open :: 비보안 네트워크)
authmodes = ['Open', 'WEP', 'WPA-PSK', 'WPA2-PSK', 'WPA/WPA2-PSK']

# 네트워크 장비(공유기, 핫스팟, ...) 정보
# ssid :: 네트워크 이름
# RSSI :: 네트워크 신호 세기 (음수로 표현, 0에 가까울수록 강한 세기)
# authmode :: 네트워크 인증/보안 방식 (숫자가 원본값)
# channel :: 네트워크 신호가 통행하는 통로 번호
# hidden :: 이름 숨김 여부 표시
# bssid :: 네트워크 공유기의 고유 식별 주소 (공유기 한 대에 여러 주소 존재)
for (ssid, bssid, channel, RSSI, authmode, hidden) in sta_if.scan():
    print("* {:s}".format(ssid))
    if 0 <= authmode < len(authmodes):    # 인증/보안 방식 값을 숫자로 불러오기
        auth_desc = authmodes[authmode]
    else:
        auth_desc = "Unknown"    # 지정된 방식 중에 없다면, Unknown 처리

    print("   - Auth: {} {}".format(auth_desc, '(hidden)' if hidden else ''))
    print("   - Channel: {}".format(channel))
    print("   - RSSI: {}".format(RSSI))
    print("   - BSSID: {:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}".format(*bssid))
    print()
