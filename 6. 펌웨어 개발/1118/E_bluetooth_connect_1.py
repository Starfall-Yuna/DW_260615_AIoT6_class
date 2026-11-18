import bluetooth, ble_simple_peripheral, time
from machine import Pin

# 42번 핀에 연결된 초록 LED 설정
green_led = Pin(42, Pin.OUT)

# 블루투스 설정
ble = bluetooth.BLE()
p = ble_simple_peripheral.BLESimplePeripheral(ble, name='pyD_1111')

# 블루투스로 데이터를 수신했을 때 실행
def on_rx(read):
    print("RX", read)

    if read == b'1':
        green_led.value(1)
        print("LED ON")

    elif read == b'0':
        green_led.value(0)
        print("LED OFF")

# 블루투스 데이터 수신 함수 등록
p.on_write(on_rx)

# nRF Connect 어플 설치