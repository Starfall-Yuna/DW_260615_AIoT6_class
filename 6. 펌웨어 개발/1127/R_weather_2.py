import network
import time
import urequests

# 공유기의 이름, 비밀번호 + 접속할 url주소
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

# 접속한 url에 있어, "첫째 주 평년 평균기온" 조회
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
    # 와이파이 연결되었다면,
    if wifi_connect():
        try:
            # url로 접속 시도
            response = urequests.get(url)
            # 접속에 성공하였다면,
            if response.status_code == 200:
                print("HTTP GET 요청 성공!")
                
                # 지정된 온도값 불러오기
                temp = extract_temp_and_reh(response.text)
                if temp is not None:
                    print("온도:", temp)
            else:
                print("HTTP GET 요청 실패. 상태 코드:", response.status_code)
        except Exception as e:
            print("HTTP GET 요청 중 오류 발생:", e)

if __name__ == "__main__":
    main()
