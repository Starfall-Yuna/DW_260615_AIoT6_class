# Python 주석은 이렇게

# Python 설치
#   1. Python.org 원하는 버전 설치 (.exe 파일)
#   2. vscode 확장팩 설치

# 출력문 :: print()
print('Hello World!')
print('줄바꿈은 하던 것처럼 \n하면 됩니다.')
print('''
여러줄에 걸쳐
출력을
해볼 수도 있습니다.
''')
print('이렇게', '끊어서도', '됩니다')
print('이렇게', '끊어서도', '됩니다', sep=',')  # seperator(구분자)를 ','로 지정

# 변수
# 변수 초기화 :: [변수이름] = [값]
name = 'Lee'
grade = 4
score = 80.5
print(name, grade, score)
print(type(name), type(grade), type(score))
# type() :: 값의 자료형 확인
# 기본 자료형 :: str(문자열), int(정수), float(실수), bool(진위)

# (참고) 강제 형변환
print(int(score))   # 실수 -> 정수

# 입력문 :: input()
input1 = input('아무거나 입력해주세요. ')
print(input1, type(input1))     # str형으로 입력받음
input2 = int(input('정수로 입력됩니다. '))
print(input2, type(input2))     # int형으로 입력받음