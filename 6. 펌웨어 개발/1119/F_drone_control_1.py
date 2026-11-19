import bluetooth,ble_simple_peripheral,time

ble = bluetooth.BLE()
p = ble_simple_peripheral.BLESimplePeripheral(ble,name='pyD_1111')

d = drone.DRONE(flightmode = 1,debug = 0)

# 캘리브레이션 :: 드론을 띄우기 전, 준비 동작 (오차 보정)
def do_calibration():
    green_led = Pin(42,Pin.OUT)
    while True:
        print(d.read_cal_data())
        if d.read_calibrated():
            print(d.read_cal_data())
            green_led.off()
            break
        green_led.on()
        time.sleep_ms(50)
        green_led.off()
        time.sleep_ms(50)

# 블루투스로 데이터 수신 반응 함수
def on_rx(read):
    # 조종값 저장
    # (Roll(좌우 기울기), Pitch(앞뒤 기울기), Yaw(회전), Throttle(추력))
    control_data = [None] * 4
    
    # 드론의 값 중에 4개 조종값 추출
    # 드론 ---(블루투스 신호)---> Thonny (이때, 전달값에 변형 발생)
    # 변형된 값을 원래 값으로 복원 (-100 실행)
    for i in range(4):
        control_data[i] = read[i+1] - 100
    print("="*50)
    print("rol:",control_data[0])
    print("pit:",control_data[1])
    print("yaw:",control_data[2])
    print("thr:",control_data[3])
    
    print("="*50)
    for i in range(len(read)):
        print(i,read[i])
        # read[0] :: 헤더
        # read[1] :: Roll값
        # read[2] :: Pitch값
        # read[3] :: Yaw값
        # read[4] :: Throttle값
        # read[5] :: 명령어 (136 정지, 24 이륙, 72 착륙, ..., 해당 코드랑은 상관X)
    print("="*50)
    
    for i in range(4):
        control_data[i] = read[i+1] - 100
    
    print('control:',control_data)

do_calibration()
p.on_write(on_rx)
