# 상속 : "물려받다", 다른 클래스 멤버 물려받아 자기 것처럼 사용
#   => 클래스 간 관계 형성

class Phone:
    def __init__(self):
        # name, number 필드 생성
        self.name = 'None'
        self.number = '000-0000-0000'
    def showNumber(self):
        print('번호:', self.number)

p1 = Phone()
p1.showNumber()

# < 상속받기 >
# class 클래스명(상속받을_클래스명):
#     추가 구성요소 정의

class SmartPhone(Phone):
    # 파이썬에서는 자동으로 부모 클래스 __init__() 실행X (강제X)
    #   Phone 클래스 __init__() 실행X 객체 생성 가능
    def __init__(self):
        # 부모 생성자를 통해서, name number 필드 생성
        super().__init__()      # Phone 클래스의 생성자 실행
        # os 필드 생성
        self.os = 'AOS'

    # 자기 자신에서의 필드 접근하는 메소드
    def showOS(self):
        print('OS:', self.os)
    # 부모 클래스의 필드 접근하는 메소드
    def showInfo(self):
        print('이름:', self.name)
        print('번호:', self.number)
        print('OS:', self.os)

sp1 = SmartPhone()
sp1.showNumber()
sp1.showOS()
sp1.showInfo()