import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 평면도에 점을 표현하기 위한 클래스
#       => 필드 : x좌표, y좌표
class Point:
    # 생성자 정의 (2개의 값을 받아, x좌표/y좌표 값 설정)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 메소드 정의
    def showInfo(self):
        print('x좌표:', self.x)
        print('y좌표:', self.y)
    def draw(self):     # 좌표 정보 기반으로, 평면도 그리기
        print('점 그리기 실행')

        # plot()로 도형 그리기
        # 원형 펜('o')으로 도형 표현
        # 10 사이즈의 펜으로 도형 그림
        # 펜의 색상을 검정(black)으로 설정
        plt.plot(self.x, self.y, marker='o', markersize='10', c='k')

# Point를 통해, 2개의 점 생성
p1 = Point(2, 3)
p2 = Point(-1, -3)
p1.showInfo()
p2.showInfo()

p1.draw()
p2.draw()
plt.xlim(-5, 5)     # 평면도의 x축 영역 지정 (-5 ~ 5)
plt.ylim(-5, 5)     # 평면도의 y축 영역 지정 (-5 ~ 5)
plt.show()


# Circle 클래스 :: draw() 오버라이딩
#   => x좌표, y좌표(원의 중심), 반지름
class Circle(Point):
    def __init__(self, x, y, r):
        # 원의 중심(x, y) 필드 설정
        super().__init__(x, y)
        # 반지름 필드 설정
        self.radius = r

    # draw() 오버라이딩 (Point의 draw() 재정의)
    def draw(self):
        print('원 그리기 실행')

        # 원 생성 (중심 좌표, 반지름)
        circle = patches.Circle((self.x, self.y), self.radius,
                                fill=False, color='b')

        # 현재 그래프에 원 추가
        plt.gca().add_patch(circle)

c1 = Circle(1, 0, 2)
c1.draw()
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.show()


# Point 클래스를 상속받는 Rectangle 클래스 생성
#   => 필드 :: x좌표, y좌표, 너비, 높이
#   => 메소드 :: draw() 오버라이딩  (주어진 값들 기반 사각형 그리기)
#       (사각형 그리는 patches 또는 plt 함수 찾아보기)
class Rectangle(Point):
    def __init__(self, x, y, w, h):
        # x좌표, y좌표 필드 생성
        super().__init__(x, y)
        # 너비, 높이 필드 생성
        self.width = w
        self.height = h
    def draw(self):
        print('사각형 그리기 실행')

        # 사각형 생성 (시작 좌표, 너비, 높이)
        rect = patches.Rectangle((self.x, self.y),
                                 self.width, self.height,
                                 fill=False, color='g')

        # 현재 그래프에 사각형 추가
        plt.gca().add_patch(rect)
r1 = Rectangle(-3, -2, 3, 2)
r1.draw()
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.show()