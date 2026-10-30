# 자바 : 부모 클래스 생성자 실행 후, 자식 클래스 생성자 실행 강제
# 파이썬 : 위 사항이 선택적

class Person:
    def __init__(self, n, a):
        # name, age 필드 생성
        self.name = n
        self.age = a
    def printAny():
        print('출력 테스트')

# super() :: 부모 클래스 접근
class Student(Person):
    def __init__(self):
        # 부모 생성자 실행 -> name, age 필드 생성
        # super().__init__('Lee', 20)

        # grade, score 필드 생성
        self.grade = 1
        self.score = 80

s = Student()   # 사용O 멤버 : grade, score, printAny()
print(s.name, s.age, s.grade, s.score)
s.printAny()