from machine import Pin
import time
import dht

dht11=dht.DHT11(Pin(18))

try :
    while True:
        dht11.measure()  
        temp = dht11.temperature()
        humi = dht11.humidity()
        
        # 온도, 습도의 값이 비정상적이라면,
        if (temp ==None) or (humi ==None):
            print("센서 에러")
        else:   # 온도, 습도의 값이 정상적이라면, 
            print(f"온도:{temp}°C  습도:{humi}RH")
        time.sleep(1.0)

except :
    pass
