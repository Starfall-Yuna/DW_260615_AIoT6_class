# 함수 :: 명령문을 묶은 것
# < 함수 생성 >
# def 함수이름(매개변수, ...):
#     함수내용
# < 함수 호출 >
#   함수이름(값)

def hello():    # hello 이름의 함수 생성
    print('Hello World')
def hi(s: int|float):   # 's에는 int 또는 float값 들어갈 수 있다' 안내
    print(s)
hello()     # hello() 실질적인 실행
hi(5.5)

# return(반환)문이 있는 함수
def add(n1, n2):    # 2개의 값 요청
    print('덧셈을 수행합니다')
    return n1+n2    # 1개의 값 반환(결과로 제시)
def sub(n1, n2):
    print('뺄셈을 수행합니다')
    return n1-n2
def mul(n1, n2):
    print('곱셈을 수행합니다')
    return n1*n2
def div(n1, n2):
    print('나눗셈을 수행합니다')
    return n1/n2
print(add(1, 2))    # n1=1, n2=2    -> print 수행 후, 3 받아옴
print(sub(1, 2))
print(mul(1, 2))
print(div(1, 2))

# 중요한 거 아님... 함수의 가독성 높이기
# 매개변수, 반환값 자료형 안내 (문법적인 제약X)
def plus(n1: int|float, n2: int|float) -> int|float:
    print('덧셈을 수행합니다')
    return n1+n2

# 사칙연산 결과 한번에 return
def calc(n1, n2):
    return n1+n2, n1-n2, n1*n2, n1/n2
result = calc(1, 2)     # 4개의 사칙연산 결과를 result에 전달
print(result)
print(type(result))     # 튜플로 전달, 수정X

# 매개변수 기본값 설정
def welcome(name='홍길동'):
    print(name, '님, 환영합니다!!!')
welcome('이유나')