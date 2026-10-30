# 두 수의 합을 return하는 함수와
def plus(a, b):
    return a+b

# 두 수의 차(+)를 return하는 함수를 작성한 뒤
def minus(a, b):
    result = a-b
    if result < 0:
        result *= -1    # abs() 기능
    return result

# 함수 외부에서 2개의 정수를 입력받고
input1 = int(input())
input2 = int(input())

# 두 입력값에 대한 합과 차를 함수들을 통해 구하여 출력
print(plus(input1, input2))
print(minus(input1, input2))

# (ex1) 30 50 입력  => 80, 20 출력
# (ex2) 50 30 입력  => 80, 20 출력
#   < 두 수의 차이에 대해서 음수값 출력X >
