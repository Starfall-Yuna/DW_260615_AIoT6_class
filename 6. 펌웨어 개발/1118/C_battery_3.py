from machine import Pin,ADC
import time

adc = ADC(Pin(2))

try:
    while True:
        # voltage :: adc 자체의 일련의 전압값을 실제 전압값으로 변환한 값
        voltage = adc.read()/4095*5.02*0.96
        # percent :: 위 실제 전압값을 배터리 잔량으로 변환한 값
        percent = (voltage - 3.0) / (4.25 - 3.0) * 100
        print(percent)
        time.sleep(1.0)

except KeyboardInterrupt:
    print("코드를 종료합니다.")