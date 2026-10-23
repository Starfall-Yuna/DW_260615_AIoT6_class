# 조건문 (if - elif - else)
# 반복문 (while, for)

# "들여쓰기" 중첩 관계 잘 표현하기

i = 0
while i <= 20:      # i = 0 ~ 20
    if i%3 == 0:    # 현재 i가 3의 배수일 때 
        print(i, end=' ')
    i += 1      # 0 -> 1 -> 2 -> ... -> 20 -> 21(반복문 종료)
print()

# break
j = 1
while True:     # 1. "일단은 반복하라", j는 1부터 시작
    if j == 10: # 3. j가 10과 같다면, break 실행
        break
    print(j, end=' ')
    j += 1      # 2. j에 1씩 증가 
# 4. break 만나면, 여기로 이동 (탈출)
print()

# continue
k = 1
while k <= 10 :     # k = 1 ~ 10
    # continue 만나면, 여기로 이동
    k += 1
    if k%2 != 0:    # k가 홀수일 때, continue 실행
        continue

    print(k, end=' ')
print()