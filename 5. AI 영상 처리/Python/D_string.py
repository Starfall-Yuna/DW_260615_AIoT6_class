first = '파이썬'
second = '프로그래밍'
print(first, second)

# +로 문자열 연결
final = first + second
print(final)
# *로 문자열 반복
print(final*3)

print(first[0])
print(final[5])

# 문자열 슬라이싱
# final = '파이썬프로그래밍'
print(final[0:3])   # 0번 글자부터 3번('프') 이전 글자까지
print(final[3:])    # 3번 글자부터 끝까지
print(final[:3])    # 시작부터 3번('프') 이전 글자까지

# 문자열 길이 확인 :: len()
print(len(final))       # 길이 :: 8
print(len(final[3:]))   # 길이 :: 5

# 특정 문자열을 입력받을 때, 아래의 규칙대로 출력하도록 하여라.
#   -> 입력받는 영문자의 길이는 정해져있지 않으나 뒤에 붙는 숫자는 반드시 4개이다.
# (ex1) abcdefg1234     -> abcdefg****
# (ex2) qwer9999        -> qwer****
# (ex3) test7735        -> test****
# (ex4) example1111     -> example****
#    뒤에서 몇번째까지 슬라이싱하는 방법 찾아보기

text = input('문자열을 입력하세요 > ')

front = text[:-4]      # 시작부터 "끝에서 4번째" 이전까지
back = '****'
result = front + back

print(result)