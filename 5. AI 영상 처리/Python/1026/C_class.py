# 객체 : "실세계에 존재하는 모든 것", 클래스를 통해 만들어진 것
# 클래스 : 객체를 만들기 위한 틀/양식
# 인스턴스 : 객체 하나하나

# 클래스 생성
# class 클래스명:
#     클래스 구성요소 정의 (멤버변수, 멤버함수, 생성자)

class Student:
    pass        # 아직 적을 내용이 없으면, pass 사용

# 객체 생성
# 인스턴스명 = 클래스명()
s = Student()
print(type(s))  # Student 클래스 통해 생성되었음 확인
print()


# 클래스 구성요소
# - 필드(멤버변수, 상태값)
# - 생성자(__init__): 객체 생성 시 실행
# - 메소드(멤버함수, 행위)

class Student:
    # 생성자 선언
    def __init__(self):      # self :: 만들어지는 인스턴스 자신
        # 필드를 생성자에서 만듬 (name, age)
        self.name = 'Lee'
        self.age = 18

    # 메소드 선언
    def intro(self):
        print('이름:', self.name)
        print('나이:', self.age)
    def isAdult(self):
        if self.age >= 20:
            print('성인입니다.')
        else:
            print('미성년자입니다.')

# 객체 생성 (생성자 실행)
# 인스턴스명 = 생성자_호출
s1 = Student()
    # 생성자 실행 -> name 필드 생성하면서 'Lee'값 설정, age 필드 생성하면서 18 값 설정
print(s1)       # 출력되긴 하지만, 내용 확인X
print(s1.name, s1.age)

s1.name = 'Park'
s1.age = 19
print(s1.name, s1.age)

s1.intro()
s1.isAdult()