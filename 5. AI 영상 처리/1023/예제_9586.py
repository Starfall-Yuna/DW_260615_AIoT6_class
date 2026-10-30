# 문자열 리스트 생성
word = ["champion", "tel", "pencil", "jungol", "olympiad",
        "class", "information", "lesson", "book", "lion" ]

# 문자 입력받기 (문자 1개 입력받는 전제)
ch = input('문자를 입력하세요. ')

# ch로 시작하는 리스트 요소 검색
for item in word:   # item :: "champion" -> "tel" -> ... -> "lion"
    if item[0] == ch:   # item의 첫 문자가 ch일때 
        print(item)