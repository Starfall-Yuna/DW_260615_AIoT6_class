# break :: "중단점", 반복문 탈출
# continue :: 반복문의 시작점(:) 이동

num = 0
while True:     # 무한반복문 :: "일단은 반복하라."
    num += 1

    if num == 10:
        break       # while문 안에 중첩된 if에 속해있음 (들여쓰기 2번)
    elif num%2 == 0:
        continue    # 짝수일 때, 반복문의 처음 이동

    print(num)
# break 만나면, 여기로 이동