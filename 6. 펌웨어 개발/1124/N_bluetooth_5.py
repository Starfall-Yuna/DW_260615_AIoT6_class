# [ 문제 ]
# 어플로 아래와 같은 입력을 드론으로 보낼때, 아래와 같이 동작하도록 하여라.
#  - 어플로 'T' 입력 시, 드론에서는 온도에 대한 정보를 어플로 전송하여 출력
#  - 어플로 'H' 입력 시, 드론에서는 습도에 대한 정보를 어플로 전송하여 출력
#  - 어플로 'ALL' 입력 시, 드론에서는 온도 및 습도에 대한 정보를 어플로 전송하여 출력

import bluetooth, ble_simple_peripheral
import time
from machine import Pin
import dht

# 블루투스 기능 활성화 + 기기 생성
ble = bluetooth.BLE()
p = ble_simple_peripheral.BLESimplePeripheral(ble, name='pyD_1111')

# 온습도센서 핀 설정
dht11 = dht.DHT11(Pin(18))

# 드론 장치(어플)에서 신호를 보낼 때, 수행할 내용 정의
def on_rx(read):
    # read값에서 유효한 값만 추출
    # (ex) b'T\r\n' 값 -> 'T' 추출
    print('원본:', read)
    data = read.decode('utf-8').strip()
    print('명령어:', data)
    
    dht11.measure()
    temp = dht11.temperature()
    humi = dht11.humidity()
    
    # T 명령어에 대한 수행 내용
    if data == 'T':
        p.send('온도:' + str(temp) + '\r\n')
    # H 명령어에 대한 수행 내용
    elif data == 'H':
        p.send('습도:' + str(humi) + '\r\n')
    # ALL 명령어에 대한 수행 내용
    elif data == 'ALL':
        p.send('온도:' + str(temp) + ', ' + '습도:' + str(humi) + '\r\n')
p.on_write(on_rx)


