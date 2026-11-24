import bluetooth,ble_simple_peripheral
import time
from machine import Pin
import dht

ble = bluetooth.BLE()
p = ble_simple_peripheral.BLESimplePeripheral(ble,name='pyD_1111')

# 온습도센서 핀 설정
dht11=dht.DHT11(Pin(18))

# 드론 장치(어플) -> 프로그램, 값 전송할 때 수행할 내용
def on_rx(read):
    print("RX:", read)
p.on_write(on_rx)

try:
    while True:   # 2초 간격으로 실시간 수행
        if p.is_connected():
            # 온습도 데이터 측정
            dht11.measure()  
            temp = dht11.temperature()
            humi = dht11.humidity()
            
            if (temp ==None) or (humi ==None):
                print("센서 에러")
            else:
                # 온습도 측정이 정상적으로 되었다면
                # 온도값과 습도값에 대해 표시
                # (온도값, 습도값) 형태로 출력
                send_str = str(temp) + "," + str(humi) + "\r\n"
                p.send(send_str)
        time.sleep(2.0)

except :
    pass