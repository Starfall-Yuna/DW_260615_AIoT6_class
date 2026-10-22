# 키, 몸무게(둘 다 정수) 입력
height = int(input())
weight = int(input())

# 첫번째 줄 비만수치 출력
ob = weight + 100 - height
print(ob)

# 비만수치 0보다 크면, "Obesity" 출력
if ob > 0:
    print('Obesity')