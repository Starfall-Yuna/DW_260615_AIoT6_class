# 파이썬은 오버로딩 지원X, 오버라이딩O

class Animal:
    def speak(self):
        print('지정된 소리가 없습니다.')

# 오버라이딩 : 부모 메소드를 자식 클래스에서 "재정의"하는 문법

class Dog(Animal):
    # Dog의 speak() 다르게 동작
    def speak(self):
        print('멍멍')
class Cat(Animal):
    def speak(self):
        print('야옹')

d = Dog()
d.speak()
c = Cat()
c.speak()