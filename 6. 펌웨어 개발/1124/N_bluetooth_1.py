import bluetooth,ble_simple_peripheral
import time

# 블루투스 기능 활성화 + 검색 가능한 블루투스 장치 추가
ble = bluetooth.BLE()
p = ble_simple_peripheral.BLESimplePeripheral(ble,name='pyD_1111')

# 드론 장치 -> 프로그램으로 값 전송했을 때, 수행할 내용
def on_rx(read):
    print("RX:", read)
p.on_write(on_rx)

# 프로그램 -> 드론 장치로 하달하는 내용
cnt = 0
try:
    while True:   # 1초 간격으로 실시간 수행
        # 드론에 있는 블루투스 장치가 어딘가에 연결되었다면,
        if p.is_connected():
            # 드론 장치로 값 전송 (cnt값) + cnt 1 증가
            p.send(str(cnt)+"\r\n")
            cnt += 1
        time.sleep(1.0)
except :
    pass

# 프로그램(SW) -> 드론 장치(HW) :: 명령어 하달
# 드론 장치(HW) -> 프로그램(SW) :: 값 전송