# 딕셔너리 {} :: "사전", (영단어) : (한국어 뜻)

# menu_price 딕셔너리 내용 구상
#   아메리카노 가격은 3700원이다...
#   카페라떼 가격은 4500원이다...
menu_price = {
    '아메리카노': 3700, 
    '카페라떼': 4500,
    '카페모카': 5000
}
print(menu_price)
print(type(menu_price), len(menu_price))

# print(menu_price[0])      # keyError
print(menu_price['아메리카노'])
print(menu_price['카페라떼'])

# 딕셔너리 관련 함수
#   - 키(Key)   :: "공간의 이름", 데이터를 찾기 위한 이름  (중복X)
#   - 값(Value) :: "그 공간의 값", 실질적인 데이터
print(menu_price.items())   # 전체 요소 확인
print(menu_price.keys())    # 결과 :: '아메리카노', '카페라떼', '카페모카'
print(menu_price.values())  # 결과 :: 3700, 4500, 5000

print(menu_price['카페라떼'])
# print(menu_price['말차라떼'])       # KeyError :: 없는 이름의 공간에 접근 시도
print(menu_price.get('카페라떼'))
print(menu_price.get('말차라떼'))     # 없는 값에 대해서, None 확인
print(menu_price.get('말차라떼', 0))  # 없는 값에 대해서, 0 확인

# 요소 추가 / 수정
menu_price['말차라떼'] = 6500
menu_price['카페모카'] = 6000

# 특정 요소 삭제
menu_price.pop('말차라떼')
print(menu_price)

# 모든 요소 삭제
menu_price.clear()
print(menu_price)