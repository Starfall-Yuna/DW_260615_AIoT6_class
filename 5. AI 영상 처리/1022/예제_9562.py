count = 0       # 짝수의 개수를 저장할 변수
num = input().split()
    # 한줄 입력 전부 받고 -> ' ' 기준으로 값들 구분지음 -> "str형" 리스트로 구성
    # num[0] = '15', num[1] = '22', num[2] = '3', ...

for i in range(10): # i : 0~9
    if int(num[i])%2 == 0:
        count += 1

print('입력받은 짝수는 {}개입니다.'.format(count))


# count = 0       # 짝수의 개수를 저장할 변수
# for i in range(10):     # i = 0 ~ 9
#     # [입력 -> 짝수 판별] 10번 반복
#     num = int(input())

#     if num%2 == 0:
#         count += 1

# print('입력받은 짝수는 {}개입니다.'.format(count))