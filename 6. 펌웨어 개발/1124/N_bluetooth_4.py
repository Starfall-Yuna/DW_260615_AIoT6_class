import bluetooth, ble_simple_peripheral
import time
from machine import Pin
import dht

# 블루투스 기능 활성화 + 기기 생성
ble = bluetooth.BLE()
p = ble_simple_peripheral.BLESimplePeripheral(ble, name='pyD_1111')

# 온습도센서 핀 설정
dht11 = dht.DHT11(Pin(18))

# 버튼1, 버튼2 핀 설정(입력 모드) + 초기값(1) 설정
key1 = Pin(38, Pin.IN, Pin.PULL_UP)
prev_state1 = key1.value()
key2 = Pin(39, Pin.IN, Pin.PULL_UP)
prev_state2 = key2.value()

def on_rx(read):
    print("RX:", read)
p.on_write(on_rx)

# 버튼1 입력 감지 함수 (중복 입력 방지)
def get_key1():
    global prev_state1
    current_state = key1.value() 
    if current_state != prev_state1:
        prev_state1 = current_state
        if current_state == 0:
            return 1
    else:
        return 0
# 버튼2 입력 감지 함수 (중복 입력 방지)
def get_key2():
    global prev_state2
    current_state = key2.value() 
    if current_state != prev_state2:
        prev_state2 = current_state
        if current_state == 0:
            return 1
    else:
        return 0

previous_time = time.time()
send_interval = 2.0

try:
    while True:
        # time.sleep(2.0)와 동일
        current_time = time.time() 
        if current_time - previous_time >= send_interval:
            previous_time = current_time
            # 드론 장치가 블루투스로 연결되었을 때
            if p.is_connected():
                # 실시간 온습도 측정+출력
                dht11.measure()
                temp = dht11.temperature()
                humi = dht11.humidity()
                if (temp is None) or (humi is None):
                    print("센서 에러")
                else:
                    send_str = str(temp) + "," + str(humi) + "\r\n"
                    p.send(send_str)
        
        # 버튼1 누르면, 출력문 실행
        if get_key1():
            p.send("key1 click\r\n")
            time.sleep(0.1)
        # 버튼2 누르면, 출력문 실행
        if get_key2():
            p.send("key2 click\r\n")
            time.sleep(0.1)
except :
    pass

