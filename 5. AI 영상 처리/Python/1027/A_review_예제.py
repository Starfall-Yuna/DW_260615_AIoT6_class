# 객체, 클래스, 인스턴스 개념 (1026 폴더 >> C_class.py 참고)

# < 클래스 생성 >
# class 클래스명:
#     생성자(필드), 메소드, ...
class Book:
    pass    # 아직 적을 내용 없으면, pass 사용
# !!! 이 뒷줄로, Book 클래스 새로 만듬 -> 위에 있는 내용 소멸 !!!

# Book 클래스 생성
#   - 필드: 제목(title), 저자(author), 페이지수(pages)
#   - 생성자: 3개의 매개변수 값 받고, 3개의 필드 선언 및 값 설정
#   - 메소드:
#       - info() :: 특정 책의 제목, 저자, 페이지수 각각 출력
#       - isLong() :: 특정 책이 두꺼운지 아닌지를 출력 (페이지수가 300 이상이면 두꺼움)

class Book:
    # 생성자 __init__()
    def __init__(self, t, a, p):
        # 필드 생성, 값 설정은 생성자 안에서
        self.title = t
        self.author = a
        self.pages = p

    # 메소드 생성
    def info(self):
        print('< 책 정보 출력 >')
        print('제목:', self.title)
        print('저자:', self.author)
        print('페이지수:', self.pages, '쪽')
    def isLong(self):
        if self.pages >= 300:
            print('두껍습니다')
        else:
            print('얇습니다')

# 1) 제목, 저자, 페이지수 값 입력받기
input_t = input('제목 입력 > ')
input_a = input('저자 입력 > ')
input_p = int(input('페이지수 입력 > '))

# 2) 1)의 값들로 인스턴스 b1 생성
#   인스턴스명 = __init__ 호출
b1 = Book(input_t, input_a, input_p)

# 3) b1의 2개 메소드 실행
b1.info()
b1.isLong()