# 오버로딩 :: "매개변수 구성이 다르면" 같은 이름의 함수여도 함께 활용O
#   Java에서는 공식적 지원O, Python에서는 공식적 지원X
#       => 생성자(__init__) 오버로딩 지원X

class Student:
    def __init__(self):         # " 작동X 없는 내용 취급 (중복 선언임을 알리지 X) "
        self.name = 'Lee'
        self.age =  18
    def __init__(self, n, a):   # 생성자로써 작동 (위 init 내용을 덮어씀)
        self.name = n
        self.age = a

    def printAny(self):     # 없는 내용 취급
        print(self.name)
    def printAny(self, change):     # 정상 작동
        self.name = change
        print(self.name)

# s1 = Student()              # 에러 발생 (2개의 필요한 값 전달X)
s2 = Student('Park', 22)      # 정상 작동
print(s2.name, s2.age)

s2.printAny('Jung')