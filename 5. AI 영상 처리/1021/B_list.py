# 리스트 [] :: 순서O, 중북O, 수정O
#   => 하나의 리스트에서 서로 다른 자료형 값을 함께 저장O

intro = ['Lee', 3, 85.7, True]

subject = ['network', 'security', 'programming']
print(subject[1])
print(subject[1:3])     # 결과 :: ['security', 'programming']
print(type(subject[1:3]))

subject[1] = 'algorithm'
print(subject)

# 빈 리스트 생성 가능
goods = []
print(type(goods))

# 요소 추가
# append() :: 리스트의 끝에서 요소 추가
goods.append('pen')
goods.append('cup')
goods.append('tumbler')
print(goods)
# insert() :: 위치를 정하여 요소 추가
goods.insert(1, 'pencil')   # goods[1] 값이 'pencil'이 되게끔 삽입
goods.insert(2, 'badge')    # goods[2] 값이 'badge'이 되게끔 삽입
print(goods)

# 요소 삭제 :: pop()
goods.pop()     # 가장 뒤에 있는 요소 삭제
print(goods)
goods.pop(2)    # [2]번 요소 삭제
print(goods)

# 리스트 길이 확인 :: len()
print(len(goods))