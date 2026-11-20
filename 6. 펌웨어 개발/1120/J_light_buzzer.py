# [ 문제 ]
# 조도센서의 입력에 따라, LED 및 부저의 출력을 아래처럼 작동하는 프로그램 작성
#   조도센서 값 1000 이상이면, 파란색 LED만 킴
#   조도센서 값 200 이상 1000 미만이면, 초록색 LED만 킴
#   조도센서 값 200 미만이면, 빨간색 LED만 키면서 부저음(도-미-솔, 한번만...) 발생
# 프로그램 종료 시 LED 끄기

from machine import Pin, PWM, ADC
import time

# 조도센서, RGB LED, 부저 핀 설정
cds_sensor=ADC(Pin(8))
cds_sensor.atten(ADC.ATTN_11DB)
LED_RED = Pin(21,Pin.OUT)
LED_GREEN = Pin(47,Pin.OUT)
LED_BLUE = Pin(48,Pin.OUT)
melody_buzzer = PWM(Pin(6, Pin.OUT), freq=100, duty=0)
melody_buzzer.duty(0)

flag = 0    # 0값(부저를 울리지 않았다.)

try:
    while True:
        # 0.5초 간격으로 조도센서 값 불러오기
        cds_value = cds_sensor.read()
        print(cds_value)
        
        # 조도센서 값에 따라 동작 수행
        # - 조도센서 값 1000 이상이면, 파란색 LED만 킴
        if cds_value >= 1000:
            flag = 0    # 다시 200 미만일 때의 부저를 켜야할 때를 대비해서
            LED_RED.off()
            LED_GREEN.off()
            LED_BLUE.on()
        # - 조도센서 값 200 이상 1000 미만이면, 초록색 LED만 킴
        elif cds_value>=200 and cds_value<1000:
            flag = 0    # 다시 200 미만일 때의 부저를 켜야할 때를 대비해서
            LED_RED.off()
            LED_GREEN.on()
            LED_BLUE.off()
        # - 조도센서 값 200 미만이면, 빨간색 LED만 키면서 부저음(도-미-솔, 한번만...) 발생
        else:
            LED_RED.on()
            LED_GREEN.off()
            LED_BLUE.off()
            
            if flag == 0:    # 아직 부저를 울리지 않았을 때
                melody_buzzer.freq(261)    # 도 출력 (0.25초)
                melody_buzzer.duty(5)
                time.sleep(0.25)
                
                melody_buzzer.freq(329)    # 미 출력 (0.25초)
                melody_buzzer.duty(5)
                time.sleep(0.25)
                
                melody_buzzer.freq(392)    # 솔 출력 (0.25초)
                melody_buzzer.duty(5)
                time.sleep(0.25)
                
                melody_buzzer.duty(0)
                flag = 1     # 부저를 울렸다는 의미로 값 변경
        
        time.sleep(0.5)
except KeyboardInterrupt:
    # 프로그램 종료 시 LED 끄기
    LED_RED.off()
    LED_GREEN.off()
    LED_BLUE.off()
    print('프로그램 종료')