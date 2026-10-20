# 리스트 [] :: 순서O, 중복O, 수정O
#   => 여러 데이터 순서에 맞춰 저장할 때 사용

intro = ['Lee', 90.6, 3, True]      # 서로 다른 자료형 값 함께 저장O
print(intro)

price = [10000, 3000, 12000, 10000]
print(price)
print(price[0])     # 결과: 10000
print(price[0:2])   # 결과: [10000, 3000] -> list형태

price[3] = 5000
print(price)

# 예제
day = ['월', '화', '수', '목', '금', '토', '일']
# 위 day를 적절하게 슬라이싱하여
# 평일만 출력하는 출력문, 주말만 출력하는 출력문 작성
print('평일: ', day[:-2])
print('평일: ', day[:5])
print('주말: ', day[5:])