# 상속 :: 다른 클래스 멤버 물려받아서 사용
#   => 부모-자식 클래스 관계 형성

# 사람
class Person:
    # 생성자
    def __init__(self, n, a):
        # 필드 :: 이름(name), 나이(age)
        self.name = n
        self.age = a
    # 메소드
    def intro(self):    # 오버라이딩 예정
        print('< 인적사항 >')
        print('이름:', self.name, end=' / ')
        print('나이:', self.age)
    def isYouth(self):
        if self.age >= 19 and self.age <= 34:
            print('청년입니다')
        else:
            print('청년이 아닙니다')

p = Person('Park', 23)
p.intro()
p.isYouth()


# 직원 (Person 상속)
class Employee(Person):
    # 생성자 
    # 파이썬 :: 부모 생성자 우선 실행 강제X
    def __init__(self):
        # 필드 : 이름(name), 나이(age), 부서(depart), 급여(money)

        # - depart, money 필드 생성
        self.depart = '교무부'
        self.money = 3500000
        # - name, age 필드 생성
        super().__init__('Kim', 40)
        # super() :: 부모 클래스 지칭

    def intro(self):    # 오버라이딩 :: 부모클래스 메소드 재정의
        print('< 직원 인적사항 >')
        print('이름:', self.name, end = ' / ')
        print('나이:', self.age)
        print('부서:', self.depart, end = ' / ')
        print('급여:', self.money)

print()
e = Employee()
e.age = 45      # 부모클래스 속하는 필드값 변경O
e.intro()
e.isYouth()     # 부모클래스 있는 그대로 활용