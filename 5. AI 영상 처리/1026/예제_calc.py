# 계산기 클래스 만들기
#   - 필드 : a, b (연산을 수행할 2개의 숫자)
#   - 생성자 : 2개의 숫자 값을 받고, 이를 기반으로 필드 선언 및 값 설정
#   - 메소드 : add(), sub(), mul(), div()
#       (덧셈/뺄셈/곱셈/나눗셈 수행하는 메소드 선언)
#       (0으로 나눌 수 없는 경우의 값이라면, 에러 메시지 발생)
class Calc:
    def __init__(self, n1, n2):
        self.a = n1
        self.b = n2

    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        # 경우에 따라서, 결과값으로 제공되는 타입 다르게 설정O
        if self.b == 0:
            return '0으로 나눌 수 없습니다'
        return self.a / self.b

# 입력값에 따라 사칙연산을 수행하는 프로그램 만들기
#   => 입력 및 연산을 반복하다가, 0 0을 입력받으면 종료
while True:
    # 2개의 숫자 입력받기
    input1 = int(input('첫번째 숫자 입력 > '))
    input2 = int(input('두번째 숫자 입력 > '))
    if input1 == 0 and input2 == 0:
        print('프로그램을 종료합니다.')
        break

    # 계산을 수행하기 위한 객체 생성
    c = Calc(input1, input2)

    # c에 대하여, 사칙연산 결과를 받기
    print('덧셈:', c.add())
    print('뺄셈:', c.sub())
    print('곱셈:', c.mul())
    print('나눗셈:', c.div())