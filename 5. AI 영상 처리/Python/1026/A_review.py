# 반복문 for문
# range(시작점, 종료점 이전값, 증감값)
for number in range(2, 11, 2):      # number : 2부터 10까지, 2씩 증가
    print(number, end=' ')
print()
for number in range(4):     # number : 0부터 3까지, 1씩 증가    range(0, 4, 1)
    print(number, end=' ')
print()

# 문자열 순회
for ch in 'Programming':    # ch : 'P' -> ... -> 'g' (11번의 반복문 수행)
    print(ch, end=' ')
print()

# 컬렉션(리스트) 순회
subjects = ['수학', '과학', '영어', '역사']
for one in subjects:        # one : '수학' -> ... -> '역사' (4번의 반복문 수행)
    if one == '영어':       # '영어' 출력 생략
        continue    
    print(one)
print()
# 컬렉션(딕셔너리) 순회     (딕셔너리 개념 : 1021 폴더 참고)
#   - key :: '사과', '우유, '식빵'
#   - value :: 3, 1, 2
shopping = {
    '사과': 3, 
    '우유': 1, 
    '식빵': 2
}
for item in shopping:   # item : key값 순회
    print(item, shopping[item])
print()
# item, number <- {'사과', 3}, {'우유', 1}, {'식빵', 2}
for item, number in shopping.items():   # item, number : key값, value값 동시 순회
    print(item, number)


# 함수 :: 명령문을 묶은 것
# def 함수이름(매개변수, ...):
#     함수내용

# return문 X
def show():
    print('파이썬 싫어')
def display(name):
    print('성함:', name)
show()
display('이유나')

# return문 O
def nemo_size(width, height):
    return width*height;
print('6*4 사각형 넓이:', nemo_size(6, 4))

# 여러 값 반환하기
def division(a, b):
    return a/b, a//b, a%b
result = division(9, 4)
print(result)
print(type(result))      # 튜플 형태로 3개 결과값 받아옴

# n개의 반환값을 n개의 변수에 저장 (차후에 수정이 용이)
r1, r2, r3 = division(9, 4)
print(r1, r2, r3)

# 매개변수 기본값 설정
def welcome(name='000'):
    print(name, '님 환영합니다')
welcome()
welcome('이유나')