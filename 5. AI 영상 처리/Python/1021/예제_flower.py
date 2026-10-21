flower = {
    'rose': 10000,
    'iris': 3000,
    'stargauge': 12000,
    'lily': 9000,
    'daffodil': 3000
}

input1 = input('첫번째 꽃을 입력하세요: ')
print('첫번째 꽃 구매 가능 여부:', input1 in flower)
print()

input2 = input('두번째 꽃을 입력하세요: ')
print('두번째 꽃 구매 가능 여부:', input2 in flower)
print()

input3 = input('세번째 꽃을 입력하세요: ')
print('세번째 꽃 구매 가능 여부:', input3 in flower)
print()

sum = 0
sum += flower.get(input1, 0)    # 존재X 꽃에 대해선, sum에 0을 추가
sum += flower.get(input2, 0)
sum += flower.get(input3, 0)

print('총 가격:', sum)