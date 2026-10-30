while True:
    score = int(input('점수를 입력하세요. '))
    if score<0 or score>100:
        break

    if score>=80:
        print('축하합니다. 합격입니다.')
    else:
        print('죄송합니다. 불합격입니다.')