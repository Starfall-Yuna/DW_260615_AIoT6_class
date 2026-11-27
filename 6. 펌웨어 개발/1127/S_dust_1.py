import network
import time
import urequests

# 공유기 이름, 비밀번호 + 접속할 url
ssid = "DW503"
password = "dwa503**"
url = 'https://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=zvlXpYH9ktzxM7siJSmQjLWjpZNRb9NDe9F%2FUIhY2J6UNiRTtEbxFIlHwJTX14BTy1P4NV0FM8NZZhBOLIld6g%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0'

# https -> http 변경 (security, 원활한 접속)
if url.startswith("https"):
    url = url.replace("https", "http", 1)

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
    # 와이파이 연결되었다면,
    if wifi_connect():
        try:
            # url 접속 시도
            response = urequests.get(url)
            if response.status_code == 200:   # 접속에 성공하였다면,
                print("HTTP GET 요청 성공!")
                print("Response:")
                print(response.text)
            else:
                print("HTTP GET 요청 실패. 상태 코드:", response.status_code)
        except Exception as e:
            print("HTTP GET 요청 중 오류 발생:", e)

if __name__ == "__main__":
    main()

