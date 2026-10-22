# 리스트 [] :: 순서O, 중복O, 수정O      (서로 다른 자료형 값 함께 저장O)
menu = ['김밥', '돈까스', '김치찌개', '라면', '김밥']
print(menu)
print(type(menu), len(menu))

menu[4] = '부대찌개'
print(menu)

menu.append('국밥')
menu.insert(2, '우동')      # menu[2] 조회할때 '우동'이 되게끔 요소 추가
print(menu)

menu.pop()      # 끝에 있는 요소 제거
print(menu)
menu.pop(4)     # [4]번 요소 제거
print(menu)

# 튜플 () :: 순서O, 중복O, 수정X (수정, 추가, 삭제)
day = ('월', '화', '수', '목', '금', '토', '일', '월')
print(day)
print(type(day), len(day))

print(day[3])
# day[0] = '일'       # TypeError :: 값 수정할 수 없는 타입

# 딕셔너리 {} :: "사전", (영단어) : (단어의 뜻)
book_price = {
    'Java마스터' : 25000, 
    '웹개발의 정석' : 30000, 
    '정보처리기사 필기준비' : 32000
}
print(book_price)
print(type(book_price), len(book_price))

print(book_price.items())   # 전체 요소 확인
print(book_price.keys())    # key값 전체 확인 (책 이름 확인됌)
print(book_price.values())  # value값 전체 확인 (책 가격 확인됌)

print(book_price['Java마스터'])
# print(book_price['점프 투 파이썬'])     # KeyError : 존재X Key
print(book_price.get('점프 투 파이썬'))   # None 확인 (에러X)

book_price['점프 투 파이썬'] = 28000    # 없는 key값 -> 요소 삽입
book_price['Java마스터'] = 27000       # 존재하는 key값 -> 값 수정

# 요소 삭제 :: pop(), clear()
#   딕셔너리는 순서X -> pop() 사용 시, key값 명시
book_price.pop('Java마스터')
print(book_price)