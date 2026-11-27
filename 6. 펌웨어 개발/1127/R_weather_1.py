import network
import time
import urequests

# 공유기의 이름, 비밀번호 + 접속할 url주소
#   => "웹크롤링"
ssid = "DW503"
password = "dwa503**"
url = "https://www.kma.go.kr/repositary/xml/fct/mon/img/fct_mon1rss_108_20261126.xml" 

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

def main():
    # 와이파이가 연결되었다면,
    if wifi_connect():
        try:
            # url에 접근한 결과값 불러오기
            response = urequests.get(url)
            # 200 코드 :: 작업에 성공
            if response.status_code == 200:
                print("HTTP GET 요청 성공!")
                print("Response:")
                print(response.text)
            else:
                print("HTTP GET 요청 실패. 상태 코드:", response.status_code)
        except Exception as e:
            print("HTTP GET 요청 중 오류 발생:", e)

# __name__ :: "어떤 파일을 통해서 해당 내용을 실행하는가"에 대한 내용이 들어감
#   자기 자신의 파일을 직접 실행하면 '__main__'로 값 설정
if __name__ == "__main__":
    main()
