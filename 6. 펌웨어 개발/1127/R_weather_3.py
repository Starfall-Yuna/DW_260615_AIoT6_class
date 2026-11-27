import network
import time
import urequests

# 공유기의 이름, 비밀번호 + 접속할 url주소
ssid = "DW503"
password = "dwa503**"
url = "https://www.kma.go.kr/repositary/xml/fct/mon/img/fct_mon1rss_108_20261126.xml"
polling_interval = 10

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
    while True:
        if wifi_connect():
            try:
                response = urequests.get(url)
                if response.status_code == 200:
                    print("HTTP GET 요청 성공!")

                    temp = extract_temp_and_reh(response.text)
                    if temp is not None:
                        print("온도:", temp)
                else:
                    print("HTTP GET 요청 실패. 상태 코드:", response.status_code)
            except Exception as e:
                print("HTTP GET 요청 중 오류 발생:", e)

        time.sleep(polling_interval)
        # 10초 간격으로, 와이파이 연결 -> url 접속 -> 온도 조회/출력

if __name__ == "__main__":
    main()
