# 튜플 () :: 순서O, 중복O, 수정X
#   => 변경X 값들을 모아서 넣을 때 사용
#   => 서로 다른 자료형 값 함께 저장O

fruit = ('apple', 'banana', 'lemon', 'apple')
print(fruit[1])     # 결과 :: 'banana'
print(type(fruit), len(fruit))

# fruit[3] = 'grape'      # 수정 불가능 (에러)

# 튜플 연결(+), 튜플 요소 반복(*)
vegetable = ('carrot', 'potato')
print(fruit + vegetable)
print(vegetable * 3)

# 튜플 슬라이싱
print(fruit[1:3])   # 'banana', 'lemon' 

# 주의할 점...
print(type( [1] ))      # 결과 : <class 'list'>
print(type( (1) ))      # 결과 : <class 'int'>,     여기에서의 ()는 산술식의 괄호로 인식
print(type( (1, ) ))    # 결과 : <class 'tuple'>

# <예제>, 튜플 슬라이싱
planet = ('수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성')
print('태양-지구 사이에 있는 것들:', planet[:2])
print('태양과 가장 멀리 있는 것:', planet[-1], planet[7])

# <예제> (멤버쉽 연산자 활용)
lotto = (3, 11, 17, 25, 32, 41)
input1 = int(input('입력: '))
print('당첨 여부:', input1 in lotto)
# 입력값이 lotto 튜플에 속하는 값인지 확인하고
# 그에 따라 True/False값을 출력