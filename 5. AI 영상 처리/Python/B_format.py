py = 'python'
c = 'c'
j = 'java'

print('1.', py, '2.', c, '3.', j)
print('1.{}, 2.{}, 3.{}'.format(py, c, j))
print('1.{2}, 2.{1}, 3.{0}'.format(py, c, j))
print('1.{l3}, 2.{l1}, 3.{l2}'.format(l1='python', l2='c', l3='java'))

# f-string 방식으로, 몇번째 소수점까지 실수 표현 지정 
pi = 3.141592
print(f'{pi:.2f}')      # 소수점 둘째 자리까지 표현