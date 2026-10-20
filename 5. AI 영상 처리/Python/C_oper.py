# 연산자 :: 연산을 수행하는 기호

# type() :: 자료형 확인
print(type(3), type(3.09), type('hello'), type(False))

# 산술연산자 
print(3+2)
print(3-2)
print(3*2)
print(3**2)     # 결과 :: 9 (3의 2제곱)
print(3/2)      # 결과 :: 1.5 (실수)
print(3//2)     # 결과 :: 1 (정수, 몫)
print(3%2)      # 결과 :: 1 (정수, 나머지)

# 대입연산자 (=)

# 복합 대입 연산자
num = 5
num += 10      # num = num+10
print(num)      # 결과 :: 15
num *= 2
print(num)      # 결과 :: 30

# 비교 연산자
n1 = 5
n2 = 10
print('> 결과 :', (n1 > n2))    # 결과 :: False
print('<= 결과 :', (n1 <= n2))   # 결과 :: True
print('== 결과:', (n1==n2))     # 결과 :: False
print('!= 결과:', (n1!=n2))     # 결과 :: True

# 논리 연산자 :: and(&&), or(||), not(!)
print('조건식1 결과:', n1!=0 and n1>n2)     # 결과: False (True && False)
print('조건식2 결과:', n1==n2 or n1<n2)     # 결과: True  (False || True)
print('조건식3 결과:', not n1==0)           # 결과: True  (!(False))

# 삼항 연산자 ::
#   (Java)   [조건식] ? [참일때의 값] : [거짓일때의 값]
#   (Python) [참일때의 값] if [조건식] else [거짓일때의 값]
result = True if 5<10 else False
print(result)