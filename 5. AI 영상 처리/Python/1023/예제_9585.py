# 빈 리스트 생성
word = []

# 5개의 단어를 입력받고, 리스트에 저장
for i in range(5):
    w = input()
    word.append(w)

# 리스트 요소 출력 
for item in word:   # item으로 word 리스트 요소 하나씩 조회
    print(item)