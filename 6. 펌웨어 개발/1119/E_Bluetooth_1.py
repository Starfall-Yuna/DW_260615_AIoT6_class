import bluetooth,ble_simple_peripheral,time

# 드론 블루투스 기능 활성화 + 검색 가능한 블루투스 장치 설정
ble = bluetooth.BLE()
p = ble_simple_peripheral.BLESimplePeripheral(ble,name='pyD_1111')

def on_rx(read):
    # 휴대폰으로 수신받은 read값 출력 (문자열로 전달)
    print("RX", read)

# 블루투스 기계(p)에 있어 write 작업을 할 때, on_rx 실행
p.on_write(on_rx)
