# BasicCalc 클래스
#   - 필드 : a, b (첫번째 숫자, 두번째 숫자)
#   - 생성자 : 2개의 매개변수 값 받아서, 2개의 필드 생성 및 값 설정
#   - 메서드 :: add(), sub(), mul(), div()
#       (div() :: 0으로 나누는 경우에 에러메시지 출력)

class BasicCalc:
    # 생성자 정의
    def __init__(self, n1, n2):
        # 필드 생성, 값 설정
        self.a = n1
        self.b = n2

    # 메소드 정의
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        if self.b == 0:
            print('0으로 나눌 수 없습니다.')
            return -1
        return self.a / self.b

# BasicCalc에 대한 객체 생성 및 메소드 테스트 (a = 10, b = 3)
bc = BasicCalc(10, 3)
print('[BasicCalc]')
print('덧셈:', bc.add())
print('뺄셈:', bc.sub())
print('곱셈:', bc.mul())
print('나눗셈:', bc.div())

# SmartCalc 클래스
#       (상속을 진행하여, 필드/메소드 추가 구성하기)
#   - 필드 : a, b (첫번째 숫자, 두번째 숫자), digits(반올림하는 소수점 숫자)
#   - 생성자 :: 3개의 매개변수 값 받아서, 3개의 필드 생성 및 값 설정
#   - 메서드 :: add(), sub(), mul(), div()
#       (div() :: 오버라이딩 적용)
#           (digits에 지정된 소수점 자릿수까지 반올림하여 반환)
#           (0으로 나누는 경우에는 에러메시지 출력)
class SmartCalc(BasicCalc):
    # 생성자 정의
    def __init__(self, n1, n2, d):
        # a, b 필드 생성    -> BasicCalc(부모클래스) 생성자
        super().__init__(n1, n2)

        # digits 필드 생성
        self.digits = d

    # 메소드 정의 -> div() 오버라이딩 진행
    def div(self):
        print('[ 소수점', self.digits, '번째 자리까지 표현합니다. ]')
        if self.b == 0:
            print('0으로 나눌 수 없습니다')
            return -1
        return round(self.a / self.b, self.digits)
        #   => 10 / 3 결과값을 소수점 2번째 자리까지 반올림하여 표현

# SmartCalc에 대한 객체 생성 및 메소드 테스트 (a = 10, b = 3, digits = 2)
s = SmartCalc(10, 3, 2)
print('[SmartCalc]')
print('덧셈:', s.add())     # 부모클래스(BasicCalc) 메소드 활용
print('뺄셈:', s.sub())
print('곱셈:', s.mul())
print('나눗셈:', s.div())   # 오버라이딩 메소드 활용