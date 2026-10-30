# 정수 입력
num = int(input())

i = 1
sum = 0     # i들의 합계 저장
while i<=num:       # i = 1, 2, ..., [입력값]
    sum += i
    i += 1
print(sum)