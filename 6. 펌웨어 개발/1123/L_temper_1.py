from machine import Pin
import time
import dht

# 온습도센서 핀 설정(GPIO 18번)
dht11=dht.DHT11(Pin(18))

try :
    while True:    # "1초 간격 실시간 작동한다"
        # 온도, 습도 측정
        dht11.measure()
        # 온도, 습도 값 불러오기 + 저장
        temp = dht11.temperature()
        humi = dht11.humidity()
        print(f"온도:{temp}°C  습도:{humi}RH")
        time.sleep(1.0)

except :
    pass