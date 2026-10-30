# for문
# for [임의변수] in [range(), 문자열, ...] :
#     반복할 명령문

# range(시작점(0), 종료점+1, 증감값(1))   -> 범위 생성
for i in range(1, 11, 1):   # i를, 1부터 11 이전까지, 1씩 증가시킴
    print(i, end=' ')
print()
for i in range(5):          # range(0, 5, 1)    => 종료점으로 5가 들어감
    print(i, end=' ')
print()
for i in range(1, 21, 2):   # i를, 1부터 21 이전까지, 2씩 증가시킴
    print(i, end=' ')
print()
for i in range(20, 0, -1):  # i를, 20부터 0 이전까지, 1씩 감소시킴
    print(i, end=' ')
print()

# 문자열 순회
for alpha in 'Korean':      # alpha :: 'K' -> 'o' -> ... -> 'n' 조회
    print(alpha, end=' ')   # 총 6번의 출력문 수행
print()
# for alpha in 'Kor':       
for alpha in 'Korean'[0:3]: # alpha :: K -> o -> r 조회
    print(alpha, end=' ')

