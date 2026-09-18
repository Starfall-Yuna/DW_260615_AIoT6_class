CREATE TABLE BOOK(
    TITLE VARCHAR2(100),
    PRICE NUMBER, 
    CATEGORY VARCHAR2(50)
);

INSERT INTO BOOK VALUES ('자바 프로그래밍 입문', 28000, '프로그래밍');
INSERT INTO BOOK VALUES ('자바 웹 개발', 32000, '프로그래밍');
INSERT INTO BOOK VALUES ('자바 기초 문법', 24000, '프로그래밍');
INSERT INTO BOOK VALUES ('파이썬 프로그래밍 입문', 30000, '프로그래밍');
INSERT INTO BOOK VALUES ('파이썬 데이터 분석', 35000, '데이터분석');
INSERT INTO BOOK VALUES ('SQL 기초', 20000, '데이터베이스');
INSERT INTO BOOK VALUES ('오라클 SQL 입문', 27000, '데이터베이스');
INSERT INTO BOOK VALUES ('SQLD 자격증 대비', 29000, '자격증');
INSERT INTO BOOK VALUES ('웹 디자인 기초', 18000, '웹');
INSERT INTO BOOK VALUES ('웹 프로그래밍 입문', 26000, '웹');
INSERT INTO BOOK VALUES ('정보처리기사 필기', 31000, '자격증');
INSERT INTO BOOK VALUES ('정보처리기사 실기', 33000, '자격증');

SELECT * FROM BOOK;

-- * 책제목이 '자바'로 시작하는 데이터 필터링, 전체 칼럼 조회
SELECT * FROM BOOK
    WHERE TITLE LIKE '자바%';

-- * 책 카테고리가 '데이터'로 시작하는 데이터 필터링, 전체 칼럼 조회
SELECT * FROM BOOK
    WHERE CATEGORY LIKE '데이터%';
-- * 책제목이 '입문'으로 끝나는 데이터 필터링, 전체 칼럼 조회
SELECT * FROM BOOK
    WHERE TITLE LIKE '%입문';
-- * 책제목에 'SQL'을 포함하는 데이터 필터링, 전체 칼럼 조회
SELECT * FROM BOOK
    WHERE TITLE LIKE '%SQL%';   -- %의 위치에 있는 값이 공백이어도, 검색이 됌

-- * 가격 칼럼값이 20000에서 30000 사이인 데이터 조회, 책과 카테고리 칼럼만 조회
SELECT
    TITLE AS 책제목,
    CATEGORY AS 분류
FROM BOOK
WHERE PRICE BETWEEN 20000 AND 30000;    -- 20000 이상 30000 이하
-- * 가격 칼럼값이 18000, 20000, 24000 중 하나인 데이터 조회, 전체 칼럼 조회
SELECT * FROM BOOK
    WHERE PRICE IN (18000, 20000, 24000);
-- * 카테고리 칼럼값이 자격증, 프로그래밍 중 하나인 데이터 조회, 전체 칼럼 조회
SELECT * FROM BOOK
    WHERE CATEGORY IN ('자격증', '프로그래밍');

-- < 참고 >
-- LIKE (%, _)
--      % :: "어떤 값이 있어도 상관없다." (글자가 여러개)
--      _ :: "어떤 문자가 있어도 상관없다." (한 글자만)
INSERT INTO BOOK VALUES ('HTML/CSS 입문 도서', 25000, '웹');
SELECT * FROM BOOK
    WHERE TITLE LIKE '%입_';     -- '입' 앞으로는 어떤 값이 있어도 상관없으나, '입' 뒤로는 한 글자만 있는 데이터
-- BETWEEN
SELECT * FROM BOOK
    WHERE TITLE BETWEEN 'A' AND 'Z';    -- TITLE의 시작 글자가 'A' ~ 'Z'(아스키코드) 사이인 데이터 
        -- 책제목의 시작 글자가 대문자 알파벳인 경우
SELECT * FROM BOOK
    WHERE TITLE BETWEEN '가' AND '히';    -- TITLE의 시작 글자가 '가'~'히'(유니코드) 사이인 데이터
        -- 책제목의 시작 글자가 한글인 경우

