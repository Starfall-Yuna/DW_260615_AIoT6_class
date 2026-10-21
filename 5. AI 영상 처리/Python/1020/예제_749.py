# 1. 4개 교과목 성적 입력 (input())
#   4개 변수 생성, 입력값으로 값 삽입 (연산을 위해, 정수형 변환)
kor = int(input())
eng = int(input())
mat = int(input())
com = int(input())

# 2. 총합(sum), 평균(avg) 구하기
sum = kor + eng + mat + com
avg = sum // 4

# 3. 정답 출력
print('sum', sum)
print('avg', avg)