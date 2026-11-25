import bluetooth,ble_simple_peripheral
import time

ble = bluetooth.BLE()
p = ble_simple_peripheral.BLESimplePeripheral(ble,name='pyD_1111')

def on_rx(read):
    # 원본 데이터 확인
    print("RX:", read)
    
    # 실제 입력값 추출 (디코딩)
    decoded_data = read.decode('utf-8').strip()
    print("Decoded:", decoded_data)
    
    # , 기준으로 값 분리 (리스트 구성)
    split_data = decoded_data.split(",")
    
    for index in range(len(split_data)):
        print(index, split_data[index])

    # 요소의 개수가 4개 and 첫번째 문자열 값이 'RGB'임
    #  (ex) RGB,350,360,400
    if len(split_data) == 4 and split_data[0] == "RGB":
        r = int(split_data[1])
        g = int(split_data[2])
        b = int(split_data[3])
        print(f"Setting RGB LED to Red: {r}, Green: {g}, Blue: {b}")
        
    else:
        print("Error: Invalid command. Expected 'RGB,R,G,B'")
    
p.on_write(on_rx)

try:
    while True:
        time.sleep(1.0)
except :
    pass