# 멤버쉽 연산자 (in)
#   => 컬렉션(리스트, 튜플, 딕셔너리, ...)에 값이 포함되어 있는지를 확인
#   [값] in [컬렉션_이름]       -> True/False
#   [값] not in [컬렉션_이름]   -> True/False

l = [11, 22, 33]
t = ('Hello', 'World')
d = {'a' : 97, 'A' : 65}

print(11 in l)      # 결과 : True
print('H' not in t) # 결과 : True
print('H' in t)     # 결과 : False
print('A' in d)     # 결과 : True
print('C' in d)     # 결과 : False
print(97 in d)      # 결과 : False (97이라는 key는 존재X)