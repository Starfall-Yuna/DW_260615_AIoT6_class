# 1. 숫자 입력
score = int(input('점수를 입력하세요. '))

# 2. 입력받은 숫자로 평가 (A, B, C, D, F)
if 90<=score and score<=100:   # A: 90 ~ 100
    print('A')
elif 80<=score and score<90:   # B: 80 ~ 89
    print('B')
elif 70<=score and score<80:   # C: 70 ~ 79
    print('C')
elif 60<=score and score<70:   # D: 60 ~ 69
    print('D')
else:
    print('F')