# 학생들의 성적을 매개변수로 받아 합계와 평균을 return하는 함수 하나를 작성한 뒤
#   힌트 :: 함수의 매개변수를 리스트 []로 감안하였다.

# data 예시 :: [80, 60, 75, 55, 100]
def calcScore(data):
    sum = 0
    for item in data:
        sum += item
    avg = sum / len(data)
    return sum, avg

# 함수 외부에서 n을 입력받고, n명의 학생 성적을 입력받는다
list = []
n = int(input('학생 수를 입력하세요 > '))
for i in range(n):
    score = int(input('성적 입력 > '))
    list.append(score)

# 입력받은 성적들에 대한 합계와 평균을 위에 작성한 함수를 통해 구하여 출력하라.
print(calcScore(list))

# (ex1) n=3, 80 90 100 입력     => 270, 90 출력
# (ex2) n=5, 70 85 90 95 100 입력   => 440, 88 출력

