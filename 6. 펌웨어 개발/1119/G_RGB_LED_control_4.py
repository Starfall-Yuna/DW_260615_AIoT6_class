from machine import Pin, PWM
import time

LED_RED = PWM(Pin(21), freq=1000, duty=0)
LED_GREEN = PWM(Pin(47), freq=1000, duty=0)
LED_BLUE = PWM(Pin(48), freq=1000, duty=0)

# RGB 적절히 조합해서 7가지 색상 연출
#   (빨강, 초록, 파랑)
rainbow_colors = [
    (1023, 0, 0),     
    (1023, 200, 0),   
    (1023, 400, 0),   
    (0, 1023, 0),     
    (0, 0, 1023),     
    (200, 0, 1023),   
    (400, 0, 1023)   
]

while True:
    for color in rainbow_colors:
        LED_RED.duty(color[0])    # (1023, 200, 0) 기준으로 1023 세기 작동
        LED_GREEN.duty(color[1])  # (1023, 200, 0) 기준으로 200 세기 작동
        LED_BLUE.duty(color[2])   # (1023, 200, 0) 기준으로 0 세기 작동
        time.sleep(1.0)