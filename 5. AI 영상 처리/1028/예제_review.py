# Car(자동차) 클래스
#   - 필드 :: 브랜드(brand), 연식(year)
#   - 메소드 ::
#       - info() :: 특정 자동차 정보 출력
class Car:
    def __init__(self, b, y):
        self.brand = b
        self.year = y
    def info(self):
        print('[ 아래는 자동차 정보입니다 ]')
        print('브랜드:', self.brand)
        print('연식:', self.year)

# ElectricCar(전기자동차) 클래스
#       (Car 클래스 상속받고, 추가적인 내용 정의)
#   - 필드 :: 브랜드(brand), 연식(year), 배터리(battery)
#   - 메소드 ::
#       - info() :: 특정 전기자동차 정보 출력
#       - charge() :: 충전 완료 안내 출력 + battery값을 100으로 설정

class ElectricCar(Car):
    def __init__(self, b, y, bt):
        # - 브랜드, 연식 필드 생성
        super().__init__(b, y)
        # - 배터리 필드 생성
        self.battery = bt
    def info(self):     # 오버라이딩 진행
        print('[ 아래는 전기자동차 정보입니다 ]')
        print('브랜드:', self.brand)
        print('연식:', self.year)
        print('배터리:', self.battery)
    def charge(self):
        print('충전을 완료하였습니다')
        self.battery = 100

# Car 객체 c 생성 및 메소드 실행 테스트
#   brand = '현대', year = 2020
c = Car('현대', 2020)
c.info()

# ElectricCar 객체 e 생성 및 메소드 실행 테스트
#   brand = '테슬라', year = 2025, battery = 85
e = ElectricCar('테슬라', 2025, 85)
e.charge()
e.info()