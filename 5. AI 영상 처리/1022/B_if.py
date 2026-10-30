# 조건문(if)
# if 조건식:
#     실행할 명령문
# elif 조건식:
#     실행할 명령문
# else:
#     실행할 명령문

# Expected indented block
# * 들여쓰기 또한 파이썬 문법 일부 *    -> Tab키로 들여쓰기 오류 해결

money = 1000
if money >= 4500 :
    print('커피 구매가 가능합니다.')    # 위의 if문에 속해있는 상태
elif money >= 2000 :
    print('콜라 구매가 가능합니다.')
else :
    print('돈이 부족합니다.')

print('프로그램을 종료합니다.')     # if문과 상관없이 독립적인 print()