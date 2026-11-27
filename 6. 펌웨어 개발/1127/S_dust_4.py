import network
import time
import urequests
import json
from machine import Pin
from machine import SoftI2C
from ssd1306 import SSD1306_I2C

ssid = "DW503"
password = "dwa503**"
url = 'https://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=zvlXpYH9ktzxM7siJSmQjLWjpZNRb9NDe9F%2FUIhY2J6UNiRTtEbxFIlHwJTX14BTy1P4NV0FM8NZZhBOLIld6g%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0'
if url.startswith("https"):
    url = url.replace("https", "http", 1)

i2c = SoftI2C(sda=Pin(43), scl=Pin(44))
oled = SSD1306_I2C(128, 64, i2c)

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
    while True :
        if wifi_connect():
            try:
                response = urequests.get(url)
                if response.status_code == 200:
                    print("HTTP GET 요청 성공!")
                    text = response.text
                
                    # [openAPI Json 응답 내용 재구성하기]
                    # 줄바꿈을 기준으로 데이터 분리
                    lines = text.split("\n")
                    # 실제 JSON 데이터만 저장할 리스트
                    result = []
                    for line in lines:
                        line = line.strip()
                        # HTTP 전송용 16진수 데이터인지 확인
                        if line and all(c in "0123456789abcdefABCDEF" for c in line):
                            continue
                        result.append(line)
                    # JSON 데이터 합치기
                    text = "".join(result)
                
                    data = json.loads(text)

                    items = data["response"]["body"]["items"]

                     # 각 항목을 출력
                    for item in items:
                        if item["stationName"] == "강남대로":  # 측정소명이 "강남대로"인 경우에만 출력
                            print("시도명:", item["sidoName"])
                            print("측정소명:", item["stationName"])
                            print("측정일시:", item["dataTime"])
                            print("미세먼지(PM10) 농도:", item["pm10Value"])
                            print("초미세먼지(PM2.5) 농도:", item["pm25Value"])
                            print("\n")
                            
                            time_str = str(item["dataTime"])
                            pm10Value_str = "pm10: " + str(item["pm10Value"])
                            pm25Value = "pm25: " + str(item["pm25Value"])
                            
                            oled.fill(0)
                            oled.text(time_str, 0, 10)
                            oled.text(pm10Value_str, 20, 20)
                            oled.text(pm25Value, 20, 30)
                            oled.show()
                    
                else:
                    print("HTTP GET 요청 실패. 상태 코드:", response.status_code)
            except Exception as e:
                print("HTTP GET 요청 중 오류 발생:", e)
        
        time.sleep(10.0)

if __name__ == "__main__":
    main()

