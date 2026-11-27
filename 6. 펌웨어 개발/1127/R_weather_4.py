import network
import time
import urequests
from machine import Pin
from machine import SoftI2C
from ssd1306 import SSD1306_I2C

# 공유기의 이름, 비밀번호 + 접속할 url주소
ssid = "DW503"
password = "dwa503**"
url = "https://www.kma.go.kr/repositary/xml/fct/mon/img/fct_mon1rss_108_20261126.xml"
polling_interval = 10

# OLED 핀, 디스플레이 설정
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

# 첫째수 평균 온도 조회하는 함수
def extract_temp_and_reh(xml_text):
    try:
        temp_start = xml_text.find("<week1_local_ta_normalYear>") + len("<week1_local_ta_normalYear>")
        temp_end = xml_text.find("</week1_local_ta_normalYear>", temp_start)
        temp = xml_text[temp_start:temp_end]

#         reh_start = xml_text.find("<reh>") + len("<reh>")
#         reh_end = xml_text.find("</reh>", reh_start)
#         reh = xml_text[reh_start:reh_end]

        return temp
    except Exception as e:
        print("Error extracting data from XML:", e)
        return None

def main():
    while True:   # 10초 간격으로 반복 수행
        if wifi_connect():
            try:
                # url 접속 시도
                response = urequests.get(url)
                if response.status_code == 200:   # 접속 성공하였다면,
                    print("HTTP GET 요청 성공!")
                    
                    # 접속한 url로, 온도값 불러오기
                    temp = extract_temp_and_reh(response.text)
                    if temp is not None:
                        print("온도:", temp)
                        
                        # OLED 출력 수행
                        oled.fill(0)
                        temp_str = "temp: " + str(temp)
                        oled.text(temp_str, 20, 20)
                        oled.show()
                else:
                    print("HTTP GET 요청 실패. 상태 코드:", response.status_code)
            except Exception as e:
                print("HTTP GET 요청 중 오류 발생:", e)

        time.sleep(polling_interval)

if __name__ == "__main__":
    main()

