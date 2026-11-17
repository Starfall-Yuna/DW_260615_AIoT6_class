from machine import Pin
import time

key = Pin(0, Pin.IN, Pin.PULL_UP)
    # 0번 핀을 입력 모드로 설정 (안정적으로 전원 유지)

# 전구 on(1), off(0)
# 버튼 누르면(0), 안 누르면(1)    => 전류의 흐름과 연관O
try:
    while True:
        key_value = key.value()    # KEY 버튼 상태 불러오기
        print(key_value)
        time.sleep(0.1)            # 위 작업을 0.1초 간격으로 실행

# stop하거나 Ctrl+C 입력해서, 예외 처리
except KeyboardInterrupt:
    print("코드를 종료합니다.")
    
    
    
    
