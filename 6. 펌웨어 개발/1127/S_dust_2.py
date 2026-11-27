import network
import time
import urequests
import json

ssid = "DW503"
password = "dwa503**"
url = 'https://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=zvlXpYH9ktzxM7siJSmQjLWjpZNRb9NDe9F%2FUIhY2J6UNiRTtEbxFIlHwJTX14BTy1P4NV0FM8NZZhBOLIld6g%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0'
if url.startswith("https"):
    url = url.replace("https", "http", 1)


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
                    print("시도명:", item["sidoName"])
                    print("측정소명:", item["stationName"])
                    print("측정일시:", item["dataTime"])
                    print("미세먼지(PM10) 농도:", item["pm10Value"])
                    print("초미세먼지(PM2.5) 농도:", item["pm25Value"])
                    print("이산화질소(NO2) 농도:", item["no2Value"])
                    print("오존(O3) 농도:", item["o3Value"])
                    print("일산화탄소(CO) 농도:", item["coValue"])
                    print("아황산가스(SO2) 농도:", item["so2Value"])
                    print("통합대기환경수치(Khai) 농도:", item["khaiValue"])
                    print("미세먼지(PM10) 등급:", item["pm10Grade"])
                    print("초미세먼지(PM2.5) 등급:", item["pm25Grade"])
                    print("이산화질소(NO2) 등급:", item["no2Grade"])
                    print("오존(O3) 등급:", item["o3Grade"])
                    print("일산화탄소(CO) 등급:", item["coGrade"])
                    print("아황산가스(SO2) 등급:", item["so2Grade"])
                    print("통합대기환경수치(Khai) 등급:", item["khaiGrade"])
                    print("\n")
                
            else:
                print("HTTP GET 요청 실패. 상태 코드:", response.status_code)
        except Exception as e:
            print("HTTP GET 요청 중 오류 발생:", e)

if __name__ == "__main__":
    main()


