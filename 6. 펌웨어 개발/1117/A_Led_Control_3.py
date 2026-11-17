from machine import Pin
import time

green_led = Pin(42,Pin.OUT)

try:
    while True:
        green_led.off()     # 전구의 출력값을 0으로 설정 (off() 작동)
        time.sleep(1.0)
        green_led.on()      # 전구의 출력값을 1로 설정 (on() 작동)
        time.sleep(1.0)

except KeyboardInterrupt:
    green_led.off()
    print("코드를 종료합니다.")

