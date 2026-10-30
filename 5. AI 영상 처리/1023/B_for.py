# for문
# for [임의변수] in [range(), 문자열, 컬렉션] :
#     반복할 명령문

# 1. range(시작점, 종료점+1, 증감값) 활용
# for(int i=1; i<5; i++)
for i in range(1, 5, 1):    # i :: 1부터 시작하여 4까지 하여, 1씩 증가
    print(i, end=' ')  
print()
# for(int i=10; i>5; i--) 
for i in range(10, 5, -1):  # i :: 10부터 시작하여 6까지 하여, 1씩 감소
    print(i, end=' ')
print()
for i in range(3):          # range(0, 3, 1)
    print(i, end=' ')
print()

for ch in 'Program':        # 문자열 길이 :: 7
    if ch == 'r':
        continue        # 'r' 출력 생략해봄
    print(ch, end=' ')      # 출력문 7번 수행
print()

# 리스트 [] 순회
lunch = ['돈까스', '국밥', '짬뽕', '햄버거', '칼국수']
for item in lunch:          # item = '돈까스' -> ... -> '칼국수'
    if item == '짬뽕':      # '짬뽕' 출력 생략
        continue    
    print(item)
print()

# 딕셔너리 {} 순회
users = {
    'admin': '0000',
    'user001': '1234',
    'player2': '1111'
}
for item in users:  # key값(ID값) 조회
    print(item, users[item])
        # 'admin', users['admin']
print()
# for [key변수], [value변수] in [딕셔너리_이름].items()
for id, pw in users.items():
    print(id, pw)