from machine import Pin
import time
import dht
from machine import SoftI2C
from ssd1306 import SSD1306_I2C

dht11=dht.DHT11(Pin(18))

# OLED 핀 설정 + 디스플레이 설정
i2c = SoftI2C(sda=Pin(43), scl=Pin(44))
oled = SSD1306_I2C(128, 64, i2c) 

try :
    while True:    # 1초 간격 실시간 작동
        # 온도, 습도 측정 + 값 불러오기
        dht11.measure()  
        temp = dht11.temperature()
        humi = dht11.humidity()
        
        # 측정값 비정상적이라면,
        if (temp ==None) or (humi ==None):
            print("센서 에러")
         # 측정값 정상적이라면,
        else:
            # Thonny 상의 출력
            print(f"온도:{temp}°C  습도:{humi}RH")
            
            # 온도, 습도에 대해 OLED 상 출력
            oled.fill(0)
            oled.text("temp:"+str(temp)+"c",10,10)
            oled.text("humi:"+str(humi)+"%",10,20)
            oled.show()   # 실제로 출력 수행
        time.sleep(1.0)

except :
    oled.fill(0)
    oled.show()

