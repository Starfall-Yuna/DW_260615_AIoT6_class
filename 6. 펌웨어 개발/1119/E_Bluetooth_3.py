import bluetooth,ble_simple_peripheral,time
from machine import Pin
import drone

ble = bluetooth.BLE()
p = ble_simple_peripheral.BLESimplePeripheral(ble,name='pyD_1111')

d = drone.DRONE(flightmode = 1,debug = 0)

# 값 자체는 정상적으로 전달O
# 제대로 작동하지 않는 이유 :: 보정 계수 설정, 캘리브레이션, ... 준비 작업 없음

def on_rx(read):
    try:
        print("BLE 수신 성공!")
        print("원본 데이터:", read)
        
        button = int(read)
        if button == 136:
            print("정지 명령 수신")
            d.stop()
        elif button == 24:
            print("이륙 명령 수신")
            d.take_off(distance=120)
        elif button == 72:
            print("착륙 명령 수신")
            d.landing()
        elif button == 40:
            print("보정 명령 수신")
        elif button == 1:
            print("Button 1")
        elif button == 2:
            print("Button 2")
        elif button == 3:
            print("Button 3")
        elif button == 4:
            print("Button 4")
        
    except Exception as e:
        print("수신 오류:", e)

p.on_write(on_rx)