# 라이브러리 함수 활용
import numpy as np
import matplotlib.pyplot as plt

# 수식을 함수로 작성
def f(x):
    return x*2 + 1      # y = 2x + 1

# 그래프를 표시할 점 표현
#   arange(시작점, 종료점 이전값, 증감값)   -> 지정된 범위에서 값 생성
x = np.arange(0, 6, 1)  # x값 생성 (0~5)
print('x값:', x)

# 생성된 x값들을 수식에 넣은 값으로 => y값 구성
y = f(x)    # 1, 3, 5, 7, 9, 11
print('y값:', y)

# 그래프 표현
plt.plot(x, y)
    # (0, 1), (1, 3), ...   => 6개 좌표 생성
    # 좌표들을 평면도 표현
plt.show()