num = [10, 20, 30, 40, 50]
print('합계:', sum(num))
print('최댓값:', max(num))
print('최솟값:', min(num))
print('평균:', sum(num) / len(num))     # Numpy 라이브러리

print('-30의 절댓값:', abs(-30))
print('30의 절댓값:', abs(30))

print('3.1415 반올림 값:', round(3.1415))
print('3.9999 반올림 값:', round(3.9999))
print('3.1415 반올림 값:', round(3.1415, 3))

list = [5, 1, 3]
print(sorted(list))
print(sorted(list, reverse=True))

print(ord('a'))     # 문자 -> 아스키코드 숫자 변형
print(chr(97))      # 숫자 -> 아스키코드 문자 변형