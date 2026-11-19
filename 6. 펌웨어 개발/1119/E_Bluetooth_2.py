import bluetooth,ble_simple_peripheral,time

ble = bluetooth.BLE()
p = ble_simple_peripheral.BLESimplePeripheral(ble,name='pyD_1234')

def on_rx(read):
    # read가 "문자열 형태"로 받아옴
    
    print("="*50)
    for i in range(len(read)):
        print(i,read[i])   # 숫자로 넣어도 아스키코드 기반 인식
    print("="*50)
    
    # 1444 입력 -> 49 52 52 52 입력

p.on_write(on_rx)

