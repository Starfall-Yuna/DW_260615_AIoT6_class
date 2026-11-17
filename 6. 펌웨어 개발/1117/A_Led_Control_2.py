from machine import Pin
import time

green_led = Pin(42,Pin.OUT)

try:    # "일단은 실행한다."
    while True:
        green_led.value(0)
        time.sleep(1.0)        # 1초간 유지
        green_led.value(1)
        time.sleep(1.0)

# Stop하거나 Ctrl+C 입력해서,
except KeyboardInterrupt:   # 예외 처리
    green_led.value(0)      # 소등
    print("코드를 종료합니다.")
    # 실행 종료
