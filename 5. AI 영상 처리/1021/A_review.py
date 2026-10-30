# Python 설치 (3.13 설치) + vscode 확장팩 설치
# python 버전 확인 :: 'python --version' / 'py --version'

# vscode 실행 :: Ctrl + F5

# 출력문, 변수 활용, 입력문
# 기본 자료형 :: int, float, str, bool
name = input('이름 입력 > ')
grade = int(input('학년 입력 > '))  # 입력값을 정수로 형변환
score = 85.5
isStudent = True
print(type(name), type(grade), type(score), type(isStudent))
print(name, grade, score, isStudent)

# format (C언어의 printf()와 유사)
print('이름: {}, 학년: {}'.format(name, grade))
    # 첫번째 중괄호에는 name값, 두번째 중괄호에는 grade값

# 연산자 :: 1020의 C_oper.py 참고

# 문자열
first = 'DW'
second = '아카데미'
last = '학원'
print(first, second, last)

result = first + second + last
print(result)
print(result*3)
print(len(result))  # 결과 : 8

# 문자열 슬라이싱
print(result[0:3])  # 결과 : 'DW아'
print(result[:5])   # 결과 : 'DW아카데'
print(result[3:])   # 결과 : '카데미학원'

print(result[:-4])  # 결과 : 'DW아카'   ([4] 글자 : '데')