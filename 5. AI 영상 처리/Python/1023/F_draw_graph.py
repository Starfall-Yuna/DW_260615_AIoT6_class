import numpy as np
import matplotlib.pyplot as plt

# 1. 수식을 함수로 구성
def f(x):
    return x**2 + 2    # f(x) = x^2 + 2

# 2. 그래프를 구성하는 점들의 x값 구성
#   arange(시작점, 종료점(포함X), 증감값)
test_x = np.arange(-2, 2.1, 0.25)
print(test_x)

# 3. y값 구성
y = f(test_x)
print(y)

# 4. 그래프로 그리기
plt.plot(test_x, y)
plt.show()