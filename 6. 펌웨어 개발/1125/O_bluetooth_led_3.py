import bluetooth,ble_simple_peripheral
import time
from machine import Pin, PWM

ble = bluetooth.BLE()
p = ble_simple_peripheral.BLESimplePeripheral(ble,name='pyD_1111')

# RGB LED 출력 핀 설정 (출력 세기 조절O)
LED_RED = PWM(Pin(21), freq=1000, duty=0)
LED_GREEN = PWM(Pin(47), freq=1000, duty=0)
LED_BLUE = PWM(Pin(48), freq=1000, duty=0)

def on_rx(read):
    # 원본 데이터 확인
    print("RX:", read)
    
    # 실제 입력값 추출 (디버깅)
    decoded_data = read.decode('utf-8').strip()
    print("Decoded:", decoded_data)
    
    split_data = decoded_data.split(",")
    print(split_data)
    
    # (ex) RGB,350,360,400
    if len(split_data) == 4 and split_data[0] == "RGB":
        r = int(split_data[1])
        g = int(split_data[2])
        b = int(split_data[3])
        LED_RED.duty(r)
        LED_GREEN.duty(g)
        LED_BLUE.duty(b)
        print(f"Setting RGB LED to Red: {r}, Green: {g}, Blue: {b}")
        
    else:
        print("Error: Invalid command. Expected 'RGB,R,G,B'")
    
    print()
    
p.on_write(on_rx)

try:
    while True:
        time.sleep(1.0)
except :
    LED_RED.duty(0)
    LED_GREEN.duty(0)
    LED_BLUE.duty(0)
