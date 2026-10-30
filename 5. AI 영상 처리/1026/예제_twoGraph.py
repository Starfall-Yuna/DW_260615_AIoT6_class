# y = 2*x + 1와 y = x^2(제곱)
# 2개의 그래프를 한 화면에 그리기
#   (x값 범위 : 0 ~ 5(포함), 0.5 간격)

import numpy as np
import matplotlib.pyplot as plt

# y = 2*x + 1 수식 작성
# y = x^2 수식 작성
def f(x):
    return 2*x + 1
def g(x):
    return x**2

# x값 표시 (공통으로 사용 -> 하나만 활용)
test_x = np.arange(0, 5.1, 0.5)
# test_x2 = np.arange(0, 5.1, 0.5)

# y값 표시 (x에 따른 결과가 다름 -> 따로 활용)
y1 = f(test_x)
y2 = g(test_x)

# 그래프 표시 
plt.plot(test_x, y1)    # 직선 그래프 그리기
plt.plot(test_x, y2)   # 곡선 그래프 그리기
plt.show()  # 위에서 그려진 2개 그래프 모두 출력