import bluetooth,ble_simple_peripheral
import time

ble = bluetooth.BLE()
p = ble_simple_peripheral.BLESimplePeripheral(ble,name='pyD_1234')

def on_rx(read):
    # 전송받은 원본 데이터
    print("RX:", read)
    
    # 원본 데이터에서 실제 입력값만 추출 (디코딩)
    #   (순수 문자열 변환 + 줄바꿈 기호 제거)
    decoded_data = read.decode('utf-8').strip()
    print("Decoded:", decoded_data)
    
    # ,(쉼표) 기준으로 값 분리 (리스트 구성)
    split_data = decoded_data.split(",")
    print("Split Data:", split_data)
    print('요소 개수:', len(split_data))

p.on_write(on_rx)

try:
    while True:
        time.sleep(1.0)
except :
    pass