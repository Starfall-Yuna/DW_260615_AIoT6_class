from machine import Pin,PWM
import time

LED_RED = PWM(Pin(21),freq=1000,duty=0)
LED_GREEN = PWM(Pin(47),freq=1000,duty=0)
LED_BLUE = PWM(Pin(48),freq=1000,duty=0)

# duty를 통해, 출력값 세기 변동 (LED 밝기 조절, 0 ~ 1023)
#    0 -> 400 -> 800 -> 1023 -> ...
while True:
    LED_RED.duty(0)
    time.sleep(1.0)
    
    LED_RED.duty(400)
    time.sleep(1.0)
    
    LED_RED.duty(800)
    time.sleep(1.0)
    
    LED_RED.duty(1023)
    time.sleep(1.0)
